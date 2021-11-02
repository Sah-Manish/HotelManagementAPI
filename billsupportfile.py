from fpdf import FPDF
import os,sys
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Ankit",database="hotel")
mycursor=mydb.cursor()
try:
  with open("billgeneratorsupportfile.txt","r") as f1:
    a=f1.readline()
    x=a.split()
except:
  with open("billgeneratorsupportfile.txt","w") as f1:
    f1.write("1")

with open("billgeneratorsupportfile.txt","r") as f1:
  a=f1.readline()
  x=a.split()
pdf=FPDF("L","mm","A4")
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(100,10,"Fate's Hotel Management System",0,0)
pdf.ln(2)
pdf.ln(2)
pdf.ln(2)
pdf.ln(2)
pdf.ln(2)
pdf.cell(100,10,"Bill Number"+" "+x[0],0,2)


with open("checkout.txt","r") as c1 :
  a=c1.readline()
  x=a.split()

l1=[101,102,103,104,105,106,107,108,109,110]
l2=[201,202,203,204,205,206,207,208,209,210]
l3=[301,302,303,304,305,306,307,308,309,310]
l4=[401,402,403,404,405,406,407,408,409,410]
l5=[501,502,503,504,505,506,507,508,509,510]
l6=[601,602,603,604,605,606,607,608,609,610]
l7=[701,702,703,704,705,706,707,708,709,710]
fa=int(x[0])
if(fa in l1):
  sql="select full_name,phone,t_days from joint_room where Room_no =%s"
  mycursor.execute(sql,(fa,))
  for i in mycursor:
    x=i
  pdf.cell(100,10,"Name :     "+x[0],0,2)
  pdf.cell(100,10,"Contact :     "+str(x[1]),0,2)
  price=x[2]*4000
  total=price+2150
  pdf.cell(100,10,"Room Charge ( Number of days * Charge per Day):_____________________________"+str(price),0,2)
  pdf.cell(100,10,"Water Bill:________________________________________________________________"+str(500),0,2)
  pdf.cell(100,10,"Electricity Bill:____________________________________________________________"+str(1500),0,2)
  pdf.cell(100,10,"Wi-Fi Charge:______________________________________________________________"+str(150),0,2)
  pdf.cell(100,10,"Total:____________________________________________________________________"+str(total),0,2)
  pdf.cell(100,10,"G.S.T Added:______________________________________________________________18%",0,2)
  pdf.cell(100,10,"__________________________________________________________________________________",0,2)
  pdf.cell(100,10,"Grand Total:_______________________________________________________________"+str(total*0.18),0,2)
  pdf.cell(100,10,"__________________________________________________________________________________",0,2)
  pdf.cell(100,10,"Thanks for staying in Fate hotel",0,2)
  pdf.ln(2)
  sql="delete from joint_room where room_no=%s"
  mycursor.execute(sql,(fa,))
  mydb.commit()
  x1='joint_room'
elif(fa in l2):
  sql="select full_name,phone,t_days from general_room where Room_no =%s"
  mycursor.execute(sql,(fa,))
  for i in mycursor:
    x=i
  pdf.cell(100,10,"Name :     "+x[0],0,2)
  pdf.cell(100,10,"Contact :     "+str(x[1]),0,2)
  price=x[2]*6000
  total=price+2150
  pdf.cell(100,10,"Room Charge ( Number of days * Charge per Day):_____________________________"+str(price),0,2)
  pdf.cell(100,10,"Water Bill:________________________________________________________________"+str(500),0,2)
  pdf.cell(100,10,"Electricity Bill:____________________________________________________________"+str(1500),0,2)
  pdf.cell(100,10,"Wi-Fi Charge:______________________________________________________________"+str(150),0,2)
  pdf.cell(100,10,"Total:____________________________________________________________________"+str(total),0,2)
  pdf.cell(100,10,"G.S.T Added:______________________________________________________________18%",0,2)
  pdf.cell(100,10,"__________________________________________________________________________________",0,2)
  pdf.cell(100,10,"Grand Total:_______________________________________________________________"+str(total*0.18),0,2)
  pdf.cell(100,10,"__________________________________________________________________________________",0,2)
  pdf.cell(100,10,"Thanks for staying in Fate hotel",0,2)
  pdf.ln(2)
  sql="delete from general_room where room_no=%s"
  mycursor.execute(sql,(fa,))
  mydb.commit()
  x1='general_room'
elif(fa in l3):
  sql="select full_name,phone,t_days from deluxe_room where Room_no =%s"
  mycursor.execute(sql,(fa,))
  for i in mycursor:
    x=i
  pdf.cell(100,10,"Name :     "+x[0],0,2)
  pdf.cell(100,10,"Contact :     "+str(x[1]),0,2)
  price=x[2]*8000
  total=price+2150
  pdf.cell(100,10,"Room Charge ( Number of days * Charge per Day):_____________________________"+str(price),0,2)
  pdf.cell(100,10,"Water Bill:________________________________________________________________"+str(500),0,2)
  pdf.cell(100,10,"Electricity Bill:____________________________________________________________"+str(1500),0,2)
  pdf.cell(100,10,"Wi-Fi Charge:______________________________________________________________"+str(150),0,2)
  pdf.cell(100,10,"Total:____________________________________________________________________"+str(total),0,2)
  pdf.cell(100,10,"G.S.T Added:______________________________________________________________18%",0,2)
  pdf.cell(100,10,"__________________________________________________________________________________",0,2)
  pdf.cell(100,10,"Grand Total:_______________________________________________________________"+str(total*0.18),0,2)
  pdf.cell(100,10,"__________________________________________________________________________________",0,2)
  pdf.cell(100,10,"Thanks for staying in Fate hotel",0,2)
  pdf.ln(2)
  sql="delete from deluxe_room where room_no=%s"
  mycursor.execute(sql,(fa,))
  mydb.commit()
  x1='deluxe_room'
elif(fa in l4):
  sql="select full_name,phone,t_days from full_deluxe_room where Room_no =%s"
  mycursor.execute(sql,(fa,))
  for i in mycursor:
    x=i
  pdf.cell(100,10,"Name :     "+x[0],0,2)
  pdf.cell(100,10,"Contact :     "+str(x[1]),0,2)
  price=x[2]*10000
  total=price+2150
  pdf.cell(100,10,"Room Charge ( Number of days * Charge per Day):_____________________________"+str(price),0,2)
  pdf.cell(100,10,"Water Bill:________________________________________________________________"+str(500),0,2)
  pdf.cell(100,10,"Electricity Bill:____________________________________________________________"+str(1500),0,2)
  pdf.cell(100,10,"Wi-Fi Charge:______________________________________________________________"+str(150),0,2)
  pdf.cell(100,10,"Total:____________________________________________________________________"+str(total),0,2)
  pdf.cell(100,10,"G.S.T Added:______________________________________________________________18%",0,2)
  pdf.cell(100,10,"__________________________________________________________________________________",0,2)
  pdf.cell(100,10,"Grand Total:_______________________________________________________________"+str(total*0.18),0,2)
  pdf.cell(100,10,"__________________________________________________________________________________",0,2)
  pdf.cell(100,10,"Thanks for staying in Fate hotel",0,2)
  pdf.ln(2)
  sql="delete from full_deluxe_room where room_no=%s"
  mycursor.execute(sql,(fa,))
  mydb.commit()
  x1='full_deluxe_room'
elif(fa in l5):
  sql="select full_name,phone,t_days from gold_class_room where Room_no =%s"
  mycursor.execute(sql,(fa,))
  for i in mycursor:
    x=i
  pdf.cell(100,10,"Name :     "+x[0],0,2)
  pdf.cell(100,10,"Contact :     "+str(x[1]),0,2)
  price=x[2]*12000
  total=price+2150
  pdf.cell(100,10,"Room Charge ( Number of days * Charge per Day):_____________________________"+str(price),0,2)
  pdf.cell(100,10,"Water Bill:________________________________________________________________"+str(500),0,2)
  pdf.cell(100,10,"Electricity Bill:____________________________________________________________"+str(1500),0,2)
  pdf.cell(100,10,"Wi-Fi Charge:______________________________________________________________"+str(150),0,2)
  pdf.cell(100,10,"Total:____________________________________________________________________"+str(total),0,2)
  pdf.cell(100,10,"G.S.T Added:______________________________________________________________18%",0,2)
  pdf.cell(100,10,"__________________________________________________________________________________",0,2)
  pdf.cell(100,10,"Grand Total:_______________________________________________________________"+str(total*0.18),0,2)
  pdf.cell(100,10,"__________________________________________________________________________________",0,2)
  pdf.cell(100,10,"Thanks for staying in Fate hotel",0,2)
  pdf.ln(2)
  sql="delete from gold_class_room where room_no=%s"
  mycursor.execute(sql,(fa,))
  mydb.commit()
  x1='gold_class_room'
elif(fa in l6):
  sql="select full_name,phone,t_days from diamond_class_room where Room_no =%s"
  mycursor.execute(sql,(fa,))
  for i in mycursor:
    x=i
  pdf.cell(100,10,"Name :     "+x[0],0,2)
  pdf.cell(100,10,"Contact :     "+str(x[1]),0,2)
  price=x[2]*14000
  total=price+2150
  pdf.cell(100,10,"Room Charge ( Number of days * Charge per Day):_____________________________"+str(price),0,2)
  pdf.cell(100,10,"Water Bill:________________________________________________________________"+str(500),0,2)
  pdf.cell(100,10,"Electricity Bill:____________________________________________________________"+str(1500),0,2)
  pdf.cell(100,10,"Wi-Fi Charge:______________________________________________________________"+str(150),0,2)
  pdf.cell(100,10,"Total:____________________________________________________________________"+str(total),0,2)
  pdf.cell(100,10,"G.S.T Added:______________________________________________________________18%",0,2)
  pdf.cell(100,10,"__________________________________________________________________________________",0,2)
  pdf.cell(100,10,"Grand Total:_______________________________________________________________"+str(total*0.18),0,2)
  pdf.cell(100,10,"__________________________________________________________________________________",0,2)
  pdf.cell(100,10,"Thanks for staying in Fate hotel",0,2)
  pdf.ln(2)
  sql="delete from diamond_class_room where room_no=%s"
  mycursor.execute(sql,(fa,))
  mydb.commit()
  x1='diamond_class_room'
elif(fa in l7):
  sql="select full_name,phone,t_days from platinum_class_room where Room_no =%s"
  mycursor.execute(sql,(fa,))
  for i in mycursor:
    x=i
  pdf.cell(100,10,"Name :     "+x[0],0,2)
  pdf.cell(100,10,"Contact :     "+str(x[1]),0,2)
  price=x[2]*16000
  total=price+2150
  pdf.cell(100,10,"Room Charge ( Number of days * Charge per Day):_____________________________"+str(price),0,2)
  pdf.cell(100,10,"Water Bill:________________________________________________________________"+str(500),0,2)
  pdf.cell(100,10,"Electricity Bill:____________________________________________________________"+str(1500),0,2)
  pdf.cell(100,10,"Wi-Fi Charge:______________________________________________________________"+str(150),0,2)
  pdf.cell(100,10,"Total:____________________________________________________________________"+str(total),0,2)
  pdf.cell(100,10,"G.S.T Added:______________________________________________________________18%",0,2)
  pdf.cell(100,10,"__________________________________________________________________________________",0,2)
  pdf.cell(100,10,"Grand Total:_______________________________________________________________"+str(total*0.18),0,2)
  pdf.cell(100,10,"__________________________________________________________________________________",0,2)
  pdf.cell(100,10,"Thanks for staying in Fate hotel",0,2)
  pdf.ln(2)
  sql="delete from platinum_class_room where room_no=%s"
  mycursor.execute(sql,(fa,))
  mydb.commit()
  x1='platinum_class_room'
else:
  print("")


with open("billgeneratorsupportfile.txt","r") as f1:
  with open("temp.txt","w") as f2:  
    a=f1.readline()
    x=a.split()
    f2.write(str(int(x[0])+1))

os.remove("billgeneratorsupportfile.txt")
os.rename("temp.txt","billgeneratorsupportfile.txt")
pdf.output('hello.pdf','F')
os.system("hello.pdf")
