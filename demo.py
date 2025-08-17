import mysql.connector as myconn
import json
from decimal import Decimal  # Decimal import karna zaroori hai

# Function to handle Decimal conversion
def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)  # Ya str(obj) agar tum string chahte ho
    raise TypeError

try:
    mydb = myconn.connect(
        host="localhost",
        user="root",
        password="pk64@sanger9896",
        database="pawan_sanger"
    )
    if mydb.is_connected():
        print("✅ Database connection successful.")

    cursor = mydb.cursor(dictionary=True)
    print("✅ Cursor created successfully.")

    sql="select * from stock"
    cursor.execute(sql)
    rows=cursor.fetchall()
    print("\n")
    for tuple in rows:
        print(tuple)

    cursor.execute("SELECT company_name, price FROM stock WHERE price> 2000;")
    rows = cursor.fetchall()

    # Convert to JSON with Decimal handling
    json_output = json.dumps(rows, indent=4, default=decimal_default)
    print(json_output)
except myconn.Error as err:
    print("❌ Error:", err)

finally:
    if mydb.is_connected():
        cursor.close()
        mydb.close()
