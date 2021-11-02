from tkinter import *
import mysql.connector
from tkinter.font import Font
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Ankit",database="hotel")
mycursor=mydb.cursor()
with open('update.txt','r') as f1:
  x=f1.read()
l1=[101,102,103,104,105,106,107,108,109,110]
l2=[201,202,203,204,205,206,207,208,209,210]
l3=[301,302,303,304,305,306,307,308,309,310]
l4=[401,402,403,404,405,406,407,408,409,410]
l5=[501,502,503,504,505,506,507,508,509,510]
l6=[601,602,603,604,605,606,607,608,609,610]
l7=[701,702,703,704,705,706,707,708,709,710]
fa=int(x)
if(fa in l1):
  sql="delete from joint_room where Room_no =%s"
  mycursor.execute(sql,(fa,))
  x='joint_room'
  mydb.commit()
elif(fa in l2):
  sql="delete from general_room where Room_no =%s"
  mycursor.execute(sql,(fa,))
  x='general_room'
  mydb.commit()
elif(fa in l3):
  sql="delete from deluxe_room where Room_no =%s"
  mycursor.execute(sql,(fa,))
  x='deluxe_room'
  mydb.commit()
elif(fa in l4):
  sql="delete from full_deluxe_room where Room_no =%s"
  mycursor.execute(sql,(fa,))
  x='full_deluxe_room'
  mydb.commit()
elif(fa in l5):
  sql="delete from gold_class_room where Room_no =%s"
  mycursor.execute(sql,(fa,))
  x='gold_class_room'
  mydb.commit()
elif(fa in l6):
  sql="delete from diamond_class_room where Room_no =%s"
  mycursor.execute(sql,(fa,))
  x='diamond_class_room'
  mydb.commit()
elif(fa in l7):
  sql="delete from platinum_class_room where Room_no =%s"
  mycursor.execute(sql,(fa,))
  x='platinum_class_room'
  mydb.commit()
else:
  print("")
def val():
  value=(fa,p1.get(),n1.get(),s1.get(),t1.get(),)
  print(value)
  global x
  if(x=='joint_room'):
    print(x)
    sql="insert into joint_room(Room_no,full_name,phone,check_in_date,check_out_date) values(%s,%s,%s,%s,%s)"
    mycursor.execute(sql,value)
    mycursor.execute("update {} set T_days = Check_out_date - Check_in_date".format(x))
    mydb.commit()
  elif(x=='general_room'):
    print(x)
    sql="insert into general_room(Room_no,full_name,phone,check_in_date,check_out_date) values(%s,%s,%s,%s,%s)"
    mycursor.excute(sql,value)
    mycursor.execute("update {} set T_days = Check_out_date - Check_in_date".format(x))
    mydb.commit()
  elif(x=='deluxe_room'):
    print(x)
    sql="insert into deluxe_room(Room_no,full_name,phone,check_in_date,check_out_date) values(%s,%s,%s,%s,%s)"
    mycursor.execute(sql,value)
    mycursor.execute("update {} set T_days = Check_out_date - Check_in_date".format(x))
    mydb.commit()
  elif(x=='full_deluxe_room'):
    print(x)
    sql="insert into deluxe_room(Room_no,full_name,phone,check_in_date,check_out_date) values(%s,%s,%s,%s,%s)"
    mycursor.execute(sql,value)
    mycursor.execute("update {} set T_days = Check_out_date - Check_in_date".format(x))
    mydb.commit()
  elif(x=='gold_class_room'):
    print(x)
    sql="insert into deluxe_room(Room_no,full_name,phone,check_in_date,check_out_date) values(%s,%s,%s,%s,%s)"
    mycursor.execute(sql,value)
    mycursor.execute("update {} set T_days = Check_out_date - Check_in_date".format(x))
    mydb.commit()
  elif(x=='diamond_class_room'):
    print(x)
    sql="insert into deluxe_room(Room_no,full_name,phone,check_in_date,check_out_date) values(%s,%s,%s,%s,%s)"
    mycursor.execute(sql,value)
    mycursor.execute("update {} set T_days = Check_out_date - Check_in_date".format(x))
    mydb.commit()
  elif(x=='platinum_class_room'):
    print(x)
    sql="insert into deluxe_room(Room_no,full_name,phone,check_in_date,check_out_date) values(%s,%s,%s,%s,%s)"
    mycursor.execute(sql,value)
    mycursor.execute("update {} set T_days = Check_out_date - Check_in_date".format(x))
    mydb.commit()
  else:
    print(x)
  root=Tk()
  root.geometry('600x200')
  myfont=Font(family="Times New Roman",size=42)
  label=Label(root,text="Welcome to Fate's Hotel Management system",font=myfont).pack()
  my=Font(family="Times New Roman",size=21)
  Label(root,text='Records have been updated',font=my).pack()
  root.mainloop()
root=Tk()
root.geometry('1300x750')
myfont=Font(family="Times New Roman",size=42)
label=Label(root,text="Welcome to Fate's Hotel Management system\nEnter Updated Details",font=myfont).pack()
d=Label(root,text="NAME").place(x=500,y=140)
g=Label(root,text="MOBILE NUMBER").place(x=500,y=180)
j=Label(root,text="CHECK IN DATE (YYYYMMDD)").place(x=500,y=220)
k=Label(root,text="CHECK OUT DATE (YYYYMMDD)").place(x=500,y=260)
room=StringVar()
p1=StringVar()
p=Entry(root,textvariable=p1).place(x=700,y=140)
n1=IntVar()
n=Entry(root,textvariable=n1).place(x=700,y=180)
s1=IntVar()
s=Entry(root,textvariable=s1).place(x=700,y=220)
t1=IntVar()
t=Entry(root,textvariable=t1).place(x=700,y=260)
b=Button(root,text='Click To Add Value', command=val)
b.place(x=600,y=300)
root.mainloop()  

