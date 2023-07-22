from tabulate import tabulate
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="S020304",database="python_db")
if(con):
    print("Connected")
else:
    print("Connection Error")
def insert(name,age,city,salary,experience):
    res=con.cursor()
    sql="INSERT INTO employee(NAME,AGE,CITY,SALARY,EXPERIENCE) values(%s,%s,%s,%s,%s)"
    user=(name,age,city,salary,experience)
    res.execute(sql,user)
    con.commit()
    print("Data Inserted Successfully..")
    print("--------------------------------------------------------")
def update(name,age,city,salary,experience,id):
    res = con.cursor()
    sql = "UPDATE employee SET name=%s,age=%s,city=%s,salary=%s,experience=%s WHERE id=%s"
    user = (name, age, city, salary, experience,id)
    res.execute(sql, user)
    con.commit()
    print("Data Updated Successfully..")
    print("--------------------------------------------------------")
def select():
    res=con.cursor()
    sql="SELECT ID,NAME,AGE,CITY,SALARY,EXPERIENCE FROM employee"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["ID","NAME","AGE","CITY","SALARY","EXPERIENCE"]))
    print("--------------------------------------------------------")
def delete(id):
    res=con.cursor()
    sql="DELETE FROM employee WHERE id=%s"
    user=(id,)
    res.execute(sql,user)
    con.commit()
    print("Data Deleted Successfully...")
    print("--------------------------------------------------------")
def bulk_insert(records):
    res=con.cursor()
    sql="INSERT INTO employee (NAME,AGE,CITY,SALARY,EXPERIENCE) values(%s,%s,%s,%s,%s)"
    res.executemany(sql,records)
    con.commit()
    print("Bulk Insert Successful...")
    print("--------------------------------------------------------")

while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Bulk Insert")
    print("6.Exit")
    print("--------------------------------------------------------")
    choice=int(input("Enter Your Choice:"))
    if(choice==1):
        name=input("Enter Name:")
        age=int(input("Enter Age:"))
        city=input("Enter City:")
        salary=int(input("Enter Salary:"))
        experience=input("Enter Experience:")
        insert(name, age, city, salary, experience)
    elif(choice == 2):
        id=int(input("Enter ID:"))
        name = input("Enter Name:")
        age = int(input("Enter Age:"))
        city = input("Enter City:")
        salary = input("Enter Salary:")
        experience = input("Enter Experience:")
        update(name, age, city, salary, experience,id)
    elif(choice==3):
        select()
    elif(choice==4):
        id=int(input("Enter the ID to be delete:"))
        delete(id)
    elif(choice==5):
        records=[]
        num_records=int(input("Enter no of records to insert:"))
        for i in range(num_records):
            name=input(f"Enter name for Record {i+1} :")
            age = input(f"Enter age for Record {i+1} :")
            city = input(f"Enter city for Record {i+1} :")
            salary = input(f"Enter salary for Record {i+1} :")
            experience = input(f"Enter experience for Record {i+1} :")
            records.append((name,age,city,salary,experience))
        bulk_insert(records)
    elif(choice==6):
        quit()
    else:
        print("Invalid Choice...Please Try Again!!")
        print("--------------------------------------------------------")




