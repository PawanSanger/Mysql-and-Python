# import mysql.connector as myconn
# mydb=myconn.connect(host="localhost",user="root",password="pk64@sanger9896",database="pawan_sanger")
# if mydb.is_connected:
#     print("connection okay....")
# cursor=mydb.cursor()
# print("cursor made successfuly....")

import mysql.connector as myconn
mydb=myconn.connect(host="localhost",user="root",password="pk64@sanger9896",database="pawan_sanger")
if mydb.is_connected():
    print("connection okay...")
cursor=mydb.cursor()
print ("cursor created successfully... ")
cursor.execute("select * from stock ")
for row in cursor.fetchall():
    print(row)
    print("total row=", cursor.rowcount)




