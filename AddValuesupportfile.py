from tkinter import *
import mysql.connector
from tkinter.font import Font
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Ankit",database="hotel")
mycursor=mydb.cursor()

def val():
  value=(p1.get(),n1.get(),s1.get(),t1.get())
  x=room.get()
  if(x=='joint_room'):
    print(x)
    sql="insert into joint_room(full_name,phone,check_in_date,check_out_date) values(%s,%s,%s,%s)"
    mycursor.execute(sql,value)
    mydb.commit()
  elif(x=='general_room'):
    print(x)
    sql="insert into general_room(full_name,phone,check_in_date,check_out_date) values(%s,%s,%s,%s)"
    mycursor.execute(sql,value)
    mydb.commit()
  elif(x=='deluxe_room'):
    print(x)
    sql="insert into deluxe_room(full_name,phone,check_in_date,check_out_date) values(%s,%s,%s,%s)"
    mycursor.execute(sql,value)
    mydb.commit()
  elif(x=='full_deluxe_room'):
    print(x)
    sql="insert into full_general_room(full_name,phone,check_in_date,check_out_date) values(%s,%s,%s,%s)"
    mycursor.execute(sql,value)
    mydb.commit()
  elif(x=='gold_class_room'):
    print(x)
    sql="insert into gold_class_room(full_name,phone,check_in_date,check_out_date) values(%s,%s,%s,%s)"
    mycursor.execute(sql,value)
    mydb.commit()
  elif(x=='diamond_class_room'):
    print(x)
    sql="insert into diamond_class_room(full_name,phone,check_in_date,check_out_date) values(%s,%s,%s,%s)"
    mycursor.execute(sql,value)
    mydb.commit()
  elif(x=='platinum_class_room'):
    print(x)
    sql="insert into platinum_class_room(full_name,phone,check_in_date,check_out_date) values(%s,%s,%s,%s)"
    mycursor.execute(sql,value)
    mydb.commit()
  else:
    print(x)
  mycursor.execute("update {} set T_days = Check_out_date - Check_in_date".format(x))
  mydb.commit()
  root=Tk()
  mycursor.execute("select room_no from {}".format(x))
  for i in mycursor:
    abc=i
  l1=list(abc)
  root.geometry('600x200')
  myfont=Font(family="Times New Roman",size=42)
  label=Label(root,text="Welcome to Fate's Hotel Management system",font=myfont).pack()
  myfont=Font(family="Times New Roman",size=25)
  Label(root,text="Your Room Number is " + str(l1[0]) + ".",font=myfont).pack()
  root.mainloop()

root=Tk()
root.geometry('1300x750')
myfont=Font(family="Times New Roman",size=42)
label=Label(root,text="Welcome to Fate's Hotel Management system\nEnter your Details",font=myfont).pack()
d=Label(root,text="NAME").place(x=500,y=140)
g=Label(root,text="MOBILE NUMBER").place(x=500,y=180)
j=Label(root,text="CHECK IN DATE (YYYYMMDD)").place(x=500,y=220)
k=Label(root,text="CHECK OUT DATE (YYYYMMDD)").place(x=500,y=260)
room=StringVar()
Label(root,text="PLEASE SELECT YOUR ROOM TYPE").place(x=500,y=300)
r1=Radiobutton(root,text='JOINT ROOM',variable=room,value='joint_room').place(x=700,y=300)
r2=Radiobutton(root,text='GENERAL ROOM',variable=room,value='general_room').place(x=500,y=340)
r3=Radiobutton(root,text='DELUXE ROOM',variable=room,value='deluxe_room').place(x=700,y=340)
r4=Radiobutton(root,text='FULL DELUXE ROOM',variable=room,value='full_deluxe_room').place(x=500,y=380)
r5=Radiobutton(root,text='GOLD CLASS ROOM',variable=room,value='gold_class_room').place(x=700,y=380)
r6=Radiobutton(root,text='DIAMOND CLASS ROOM',variable=room,value='diamond_class_room').place(x=500,y=420)
r7=Radiobutton(root,text='PLATINUM ROOM',variable=room,value='platinum_class_room').place(x=700,y=420)

p1=StringVar()
p=Entry(root,textvariable=p1).place(x=700,y=140)
n1=IntVar()
n=Entry(root,textvariable=n1).place(x=700,y=180)
s1=IntVar()
s=Entry(root,textvariable=s1).place(x=700,y=220)
t1=IntVar()
t=Entry(root,textvariable=t1).place(x=700,y=260)
b=Button(root,text='Click To Add Value', command=val)
b.place(x=600,y=460)
root.mainloop()  

