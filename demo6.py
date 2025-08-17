import mysql.connector as myconn
import json
mydb=myconn.connect(host="localhost",user="teamuser",password="123@",database="pawan_sanger")
if mydb.is_connected():
    print("....................")
    print("Connection okay")
cursor=mydb.cursor()
print("cursor okay")
def add():
    id=int(input("enter id "))
    n=input("enter name ")
    age=int(input("enter age "))
    salary=int(input("enter salary "))
    s="insert into customer (id,name,age,salary)values(%s,%s,%s,%s)"
    cursor.execute(s,(id,n,age,salary))
def delete():
    name=input("enter name to delete rocord")
    s="DELETE FROM customer WHERE name=%s"
    cursor.execute(s,(name))
    print("Record deleted successfully!")
def show():
    s="select * from customer"
    cursor.execute(s)
    for i in cursor.fetchall():
        print(i)
def json_():
    s = input("enter query to change into json (only accesseble queries)")
    cursor.execute(s)
    rows=cursor.fetchall()
    json_output = json.dumps(rows, indent=4,)
    print(json_output)
choice = int(input("Enter 1 to Add, 2 to Delete, 3 to Show 4 to Json 0 to Exit: "))
if choice == 1:
    add()
elif choice == 2:
    delete()
elif choice == 3:
    show()
elif choice == 4:
    json_()
else:
    print("Exited..")

mydb.commit()
cursor.close()
mydb.close()