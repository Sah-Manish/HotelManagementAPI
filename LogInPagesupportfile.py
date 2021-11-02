from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import mysql.connector

root=Tk()
root.geometry('1300x750')
uname=StringVar()
upasswo=StringVar()
name=StringVar()
passwo=StringVar()
myfont=Font(family="Times New Roman",size=42)

def adminpage():
  root=Tk()
  root.geometry('1300x750')
  label=Label(root,text="Welcome to Fate's Hotel Management system\nSelect your choice",font=myfont).pack()
  button3=Button(root, text='Show Records',width=40,height=5,command=showrecords).place(x=300,y=300)
  button4=Button(root, text='Update Record',width=40,height=5,command=updaterecord).place(x=700,y=300)
  root.mainloop()


def updaterecord():
  import sys,os
  os.system('roominputforupdatesupportfile.py')
  
def showrecords():
  root=Tk()
  root.geometry('1300x750')
  myfont=Font(family="Times New Roman",size=42)
  label=Label(root,text="Welcome to Fate's Hotel Management system",font=myfont).pack()
  myfont=Font(family="Times New Roman",size=25)
  Label(root,text="Room_no  Full_name  Phone  Check_in_Date  Check_out_Date  Total_Days",font=myfont).pack()
  mydb=mysql.connector.connect(host="localhost",user="root",passwd="aps",database="hotel")
  mycursor=mydb.cursor()
  mycursor.execute('select * from joint_room')
  for i in mycursor:
    Label(root,text=i).pack()
    
  mycursor.execute('select * from general_room')
  for i in mycursor:
    Label(root,text=i).pack()
    
  mycursor.execute('select * from deluxe_room')
  for i in mycursor:
    Label(root,text=i).pack()
    
  mycursor.execute('select * from full_deluxe_room')
  for i in mycursor:
    Label(root,text=i).pack()
    
  mycursor.execute('select * from gold_class_room')
  for i in mycursor:
    Label(root,text=i).pack()
    
  mycursor.execute('select * from diamond_class_room')
  for i in mycursor:
    Label(root,text=i).pack()
    
  mycursor.execute('select * from platinum_class_room')
  for i in mycursor:
    Label(root,text=i).pack()
  root.mainloop()
  

def adduserq():
  myfont=Font(family="Times New Roman",size=42)
  label=Label(root,text="Welcome to Fate's Hotel Management system\nNew User Applicatiin Page",font=myfont).place(x=150,y=0)
  Label(root,text="PASSWORD").place(x=450,y=200)
  Entry(root,textvariable=uname).place(x=650,y=150)
  Entry(root,textvariable=upasswo).place(x=650,y=200)
  Button(root,text='Hide Password  ',command=adduser).place(x=800,y=200)
  Button(root,text="CLICK TO Add Administrator Id",command=addtodb).place(x=600,y=300)
  Label(root,text="   Only Administrator!    \n                            ").place(x=600,y=400)
  


  
def adduser():
  myfont=Font(family="Times New Roman",size=42)
  label=Label(root,text="Welcome to Fate's Hotel Management system\nNew User Applicatiin Page",font=myfont).place(x=150,y=0)
  Label(root,text="PASSWORD").place(x=450,y=200)
  Entry(root,textvariable=uname).place(x=650,y=150)
  Entry(root,textvariable=upasswo,show='*').place(x=650,y=200)
  Button(root,text='Show Password',command=adduserq).place(x=800,y=200)
  Button(root,text="CLICK TO Add Administrator Id",command=addtodb).place(x=600,y=300)
  Label(root,text="   Only Administrator!    \n                            ").place(x=600,y=400)
  
def addtodb():
  valuetoinsert=(str(uname.get()),str(upasswo.get()))
  sql="insert into users(User_Name,Password) values(%s,%s)"
  mycursor.execute(sql,valuetoinsert)
  mydb.commit()
  
def error():
  messagebox.showinfo('Error user name or password','You Entered A Wrong User Name Or Password !!!')

def error1():
  messagebox.showinfo('User Id Maximum !!!', 'We already have max Administrator User ID(s)')

def value():
  value=(str(name.get()),str(passwo.get()))
  a=str(name.get())
  c=str(passwo.get())
  sql="select user_name, password from users where user_name=%s"
  mycursor.execute(sql,(a,))
  b=mycursor.fetchall()
  l1=[]
  for i in b:
    l1.append(i)
  
  if((a,c) in l1):
    adminpage()
  else:
    error()
  
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Ankit",database="hotel")
mycursor=mydb.cursor()

def addusers():
  mycursor.execute("select sno from users")
  for i in mycursor:
    ids=i
  if(ids==(1,)):
    adduser()
  else:
    error1()


def val():  
  label=Label(root,text="Welcome to Fate's Hotel Management system\nAdministrator Log In Required",font=myfont).place(x=150,y=0)
  l=Label(root,text="ADMINISTRATOR USER NAME").place(x=450,y=150)
  Label(root,text="PASSWORD").place(x=450,y=200)
  Entry(root,textvariable=name).place(x=650,y=150)
  Entry(root,textvariable=passwo,show='*').place(x=650,y=200)
  Button(root,text='Show Password',command=valq).place(x=800,y=200)
  Button(root,text="CLICK TO LOG IN",command=value).place(x=600,y=300)
  Button(root,text="Create Administrator ID",command=addusers).place(x=600,y=400)
def valq():
  label=Label(root,text="Welcome to Fate's Hotel Management system\nAdministrator Log In Required",font=myfont).place(x=150,y=0)
  l=Label(root,text="ADMINISTRATOR USER NAME").place(x=450,y=150)
  Label(root,text="PASSWORD").place(x=450,y=200)
  Entry(root,textvariable=name).place(x=650,y=150)
  Entry(root,textvariable=passwo).place(x=650,y=200)
  Button(root,text='Hide Password  ',command=val).place(x=800,y=200)
  Button(root,text="CLICK TO LOG IN",command=value).place(x=600,y=300)
  Button(root,text="Create Administrator ID",command=addusers).place(x=600,y=400)
val()  
root.mainloop()









