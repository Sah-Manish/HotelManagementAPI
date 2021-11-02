from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import mysql.connector
root=Tk()
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Ankit",database="hotel")
mycursor=mydb.cursor()
l1=[]
rno=IntVar()


def value():
  mycursor.execute("select Room_no from joint_room")
  for i in mycursor:
    l1.append(i)
  mycursor.execute("select Room_no from general_room")
  for i in mycursor:
    l1.append(i)
  mycursor.execute("select Room_no from deluxe_room")
  for i in mycursor:
    l1.append(i)
  mycursor.execute("select Room_no from full_deluxe_room")
  for i in mycursor:
    l1.append(i)
  mycursor.execute("select Room_no from gold_class_room")
  for i in mycursor:
    l1.append(i)
  mycursor.execute("select Room_no from diamond_class_room")
  for i in mycursor:
    l1.append(i)
  mycursor.execute("select Room_no from platinum_class_room")
  for i in mycursor:
    l1.append(i)
  if((rno.get(),) in l1):
    with open('checkout.txt','w') as f1:
      f1.writelines(str(rno.get()))
    import sys,os
    os.system('billsupportfile.py')
    
  else:
    messagebox.showinfo('Error','Entered Room Number is not Valid')
root.geometry('600x200')
my=Font(family="Times New Roman",size=21)
Label(root,text="Welcome to Fate's Hotel Management system",font=my).pack()
Label(root,text="Enter Room Number").place(x=175,y=50)
Entry(root,textvariable=rno).place(x=300,y=50)
Button(root,text="Click To Update",command=value).place(x=250,y=101)
root.mainloop()


























