from tkinter import *
from tkinter.font import Font
import mysql.connector

def loginpage():
  import sys,os
  os.system('LogInPagesupportfile.py')


def addpage():
  import sys,os
  os.system('AddValuesupportfile.py')
  
def guestpage():
  button1=Button(root, text='Check In ',width=40,height=5,command=addpage).place(x=300,y=300)
  button2=Button(root, text='Check Out',width=40,height=5,command=removepage).place(x=700,y=300)
def removepage():
  import sys,os
  os.system('roominputforcheckoutsupportfile.py')
  
  
  

mydb=mysql.connector.connect(host="localhost",user="root",passwd="Ankit")
mycursor=mydb.cursor()
try:
  mycursor.execute("create database hotel")
except:
  print("")
mycursor.execute("show databases")

database_list=[]
for database in mycursor:
  database_list.append(database)
if("hotel" in database_list):
  mydb=mysql.connector.conne(host="localhost",user="root",passwd="aps",database="hotel")
  mycursor.execute("use hotel")
else:
  mycursor.execute("use hotel")
stable=[('deluxe_room',), ('diamond_class_room',), ('full_deluxe_room',), ('general_room',), ('gold_class_room',), ('joint_room',), ('platinum_class_room',), ('users',)]  
mycursor.execute("show tables")
table=[]
for i in mycursor:
  table.append(i)
if(stable ==  table):
  print("")
  
else:
  mycursor.execute("create table Joint_room(Room_no int AUTO_INCREMENT PRIMARY KEY CHECK (Room_no<111),Full_Name VARCHAR(255),Phone BIGINT)")
  mycursor.execute("ALTER table Joint_room ADD Check_in_date DATE")
  mycursor.execute("ALTER table Joint_room ADD Check_out_date DATE")
  mycursor.execute("ALTER table Joint_room ADD T_days int")
  mycursor.execute("ALTER table Joint_room AUTO_INCREMENT=101")
  
  mycursor.execute("create table General_room(Room_no int AUTO_INCREMENT PRIMARY KEY CHECK (Room_no<211),Full_Name VARCHAR(255),Phone BIGINT)")
  mycursor.execute("ALTER table General_room ADD Check_in_date DATE")
  mycursor.execute("ALTER table General_room ADD Check_out_date DATE")
  mycursor.execute("ALTER table General_room ADD T_days int")
  mycursor.execute("ALTER table General_room AUTO_INCREMENT=201")

  mycursor.execute("create table Deluxe_room(Room_no int AUTO_INCREMENT PRIMARY KEY CHECK (Room_no<311),Full_Name VARCHAR(255),Phone BIGINT)")
  mycursor.execute("ALTER table Deluxe_room ADD Check_in_date DATE")
  mycursor.execute("ALTER table Deluxe_room ADD Check_out_date DATE")
  mycursor.execute("ALTER table Deluxe_room ADD T_days int")
  mycursor.execute("ALTER table Deluxe_room AUTO_INCREMENT=301")

  mycursor.execute("create table Full_Deluxe_room(Room_no int AUTO_INCREMENT PRIMARY KEY CHECK (Room_no<411),Full_Name VARCHAR(255),Phone BIGINT)")
  mycursor.execute("ALTER table Full_Deluxe_room ADD Check_in_date DATE")
  mycursor.execute("ALTER table Full_Deluxe_room ADD Check_out_date DATE")
  mycursor.execute("ALTER table Full_Deluxe_room ADD T_days int")
  mycursor.execute("ALTER table Full_Deluxe_room AUTO_INCREMENT=401")

  mycursor.execute("create table Gold_Class_room(Room_no int AUTO_INCREMENT PRIMARY KEY CHECK (Room_no<511),Full_Name VARCHAR(255),Phone BIGINT)")
  mycursor.execute("ALTER table Gold_Class_room ADD Check_in_date DATE")
  mycursor.execute("ALTER table Gold_Class_room ADD Check_out_date DATE")
  mycursor.execute("ALTER table Gold_Class_room ADD T_days int")
  mycursor.execute("ALTER table Gold_Class_room AUTO_INCREMENT=501")

  mycursor.execute("create table Platinum_Class_room(Room_no int AUTO_INCREMENT PRIMARY KEY CHECK (Room_no<611),Full_Name VARCHAR(255),Phone BIGINT)")
  mycursor.execute("ALTER table Platinum_Class_room ADD Check_in_date DATE")
  mycursor.execute("ALTER table Platinum_Class_room ADD Check_out_date DATE")
  mycursor.execute("ALTER table Platinum_Class_room ADD T_days int")
  mycursor.execute("ALTER table Platinum_Class_room AUTO_INCREMENT=601")

  mycursor.execute("create table Diamond_Class_room(Room_no int AUTO_INCREMENT PRIMARY KEY CHECK (Room_no<711),Full_Name VARCHAR(255),Phone BIGINT)")
  mycursor.execute("ALTER table Diamond_Class_room ADD Check_in_date DATE")
  mycursor.execute("ALTER table Diamond_Class_room ADD Check_out_date DATE")
  mycursor.execute("ALTER table Diamond_Class_room ADD T_days int")
  mycursor.execute("ALTER table Diamond_Class_room AUTO_INCREMENT=701")

  mycursor.execute("create table IF NOT EXISTS users(sno int CHECK (sno<3),User_Name varchar(40) UNIQUE, Password varchar(64))")
try:
  mycursor.execute("insert into users value(1,'Fate','Averruncus')")
  mydb.commit()
except:
  print("")

root=Tk()
root.geometry('1300x750')
myfont=Font(family="Times New Roman",size=42)
label=Label(root,text="Welcome to Fate's Hotel Management system\nSelect Your Login",font=myfont).pack()


button1=Button(root, text='Admin',width=40,height=5,command=loginpage).place(x=300,y=300)
button2=Button(root, text='Guest',width=40,height=5,command=guestpage).place(x=700,y=300)
root.mainloop()

