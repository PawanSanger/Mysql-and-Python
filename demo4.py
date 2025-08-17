import mysql.connector as myconn
mydb=myconn.connect(host="localhost",user="root",password="pk64@sanger9896",database="pawan_sanger")
if mydb.is_connected():
    print("connection okay...")
cursor=mydb.cursor()
print ("cursor created successfully... ")
name=input("enter name")
logo=input("enter logo")
price=float(input("enter price."))
unit=int(input("enter unit."))
l_update=(input("enter date."))

s = "INSERT INTO stock (company_name, ticker_symbol, price, quantity, last_updated)  VALUES (%s, %s, %s, %s, %s)"
t=name,logo,price,unit,l_update
cursor.execute(s,t)
print("Data inserted successfully!")
mydb.commit()