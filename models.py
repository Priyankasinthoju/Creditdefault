import sqlite3 as sql
import os
currentdirectory = os.path.dirname(os.path.abspath('DATABASE_URL'))
def insertUser(FirstName,LastName,Email,Education,DateOfBirth,SSN,PhoneNumber,Gender,MaritalStatus,CreditAmount,Rpay_Status_1,Rpay_Status_2,Rpay_Status_3,Rpay_Status_4,Rpay_Status_5,Rpay_Status_6,Statement_1,Statement_2,Statement_3,Statement_4,Statement_5,Statement_6,Payment_1,Payment_2,Payment_3,Payment_4,Payment_5,Payment_6,Default_pay):
    con = sql.connect("Customer_Information.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Customer_info (FirstName,LastName,Email,Education,DateOfBirth,SSN,PhoneNumber,Gender,MaritalStatus,CreditAmount,Rpay_Status_1,Rpay_Status_2,Rpay_Status_3,Rpay_Status_4,Rpay_Status_5,Rpay_Status_6,Statement_1,Statement_2,Statement_3,Statement_4,Statement_5,Statement_6,Payment_1,Payment_2,Payment_3,Payment_4,Payment_5,Payment_6,Default_pay) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (FirstName,LastName, Email,Education, DateOfBirth,SSN,PhoneNumber,Gender,MaritalStatus,CreditAmount,Rpay_Status_1,Rpay_Status_2,Rpay_Status_3,Rpay_Status_4,Rpay_Status_5,Rpay_Status_6,Statement_1,Statement_2,Statement_3,Statement_4,Statement_5,Statement_6,Payment_1,Payment_2,Payment_3,Payment_4,Payment_5,Payment_6,Default_pay))
    con.commit()
    con.close()
def retrieveUsers():
	con = sql.connect("Customer_Information.db")
	cur = con.cursor()
	cur.execute("SELECT FirstName,LastName,Email,Education,DateOfBirth,SSN,PhoneNumber,Gender,MaritalStatus,CreditAmount,Rpay_Status_1,Rpay_Status_2,Rpay_Status_3,Rpay_Status_4,Rpay_Status_5,Rpay_Status_6,Statement_1,Statement_2,Statement_3,Statement_4,Statement_5,Statement_6,Payment_1,Payment_2,Payment_3,Payment_4,Payment_5,Payment_6,Default_pay FROM Customer_info")
	Customer_info = cur.fetchall()
	con.close()
	return Customer_info
