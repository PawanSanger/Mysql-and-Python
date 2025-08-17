import mysql.connector as myconn
import json
from decimal import Decimal

# Decimal को float में बदलने के लिए function
def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
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

    # User से price लो
    price_limit = float(input("Enter minimum price: "))

    # Parameterized query
    sql = "SELECT company_name, price FROM stock WHERE price > %s"
    cursor.execute(sql, (price_limit,))
    rows = cursor.fetchall()

    # Console output
    print("\nFetched Data:")
    for row in rows:
        print(row)

    # JSON output
    json_output = json.dumps(rows, indent=4, default=decimal_default)
    print("\nJSON Output:")
    print(json_output)

except myconn.Error as err:
    print("❌ Error:", err)

finally:
    if mydb.is_connected():
        cursor.close()
        mydb.close()
