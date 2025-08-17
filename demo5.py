import mysql.connector as myconn
mydb=myconn.connect(host="localhost",user="root",password="pk64@sanger9896",database="pawan_sanger")
if mydb.is_connected():
    print("connection okay...")
cursor=mydb.cursor()
print ("cursor created successfully... ")
company_name=input("enter company_name  ")
query="select * from stock where company_name=%s"
cursor.execute(query,(company_name,))
result=cursor.fetchone()
if result:
    print(f"the price of {company_name} is:{result[3]}")
else:
    print("Company not found in database.")
cursor.close()
mydb.close()