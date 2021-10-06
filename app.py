from sqlite3.dbapi2 import Cursor, connect
from flask import Flask, render_template, request
import sqlite3
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
import os
import models as dbHandler
currentdirectory = os.path.dirname(os.path.abspath(__file__))


app = Flask("__name__")
model = pickle.load(open('random_forest_classifier_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('webpageupdated.html')
standard_to = StandardScaler()
@app.route("/predict", methods = ['GET','POST'])
def predict():
    alert_message = False
    success_message = False
    try:
        if request.method == 'POST':

            FirstName = request.form['FirstName']
            LastName = request.form['LastName']
            Email = request.form['Email']
            Education = request.form['Education']
            if (Education == 'Graduate'):
                Education_Graduate = 1
                Education_University = 0
                Education_HighSchool = 0
                Education_Others = 0
            elif (Education == 'University'):
                Education_Graduate = 0
                Education_University = 1
                Education_HighSchool = 0
                Education_Others = 0
            elif (Education == 'Highschool'):
                Education_Graduate = 0
                Education_University = 0
                Education_HighSchool = 1
                Education_Others = 0
            else:
                Education_Graduate = 0
                Education_University = 0
                Education_HighSchool = 0
                Education_Others = 1

            Age = int(request.form['Age'])
            SSN = int(request.form['SSN'])
            PhoneNumber = int(request.form['PhoneNumber'])
            Gender = request.form['Gender']
            if (Gender == 'Male'):
                Gender_Male = 1
                Gender_Female =0
            else:
                Gender_Female = 1
                Gender_Male = 0
            MaritalStatus = request.form['MaritalStatus']
            if (MaritalStatus == 'Married'):
                MaritalStatus_Married = 1
                MaritalStatus_Single = 0
                MaritalStatus_Others = 0
            elif (MaritalStatus == 'Single'):
                MaritalStatus_Married = 0
                MaritalStatus_Single = 1
                MaritalStatus_Others = 0
            else:
                MaritalStatus_Married = 0
                MaritalStatus_Single = 0
                MaritalStatus_Others = 1
            CreditAmount = int(request.form['CreditAmount'])
            Rpay_Status_1 = int(request.form['Rpay_Status_1'])
            Rpay_Status_2 = int(request.form['Rpay_Status_2'])
            Rpay_Status_3 = int(request.form['Rpay_Status_3'])
            Rpay_Status_4 = int(request.form['Rpay_Status_4'])
            Rpay_Status_5 = int(request.form['Rpay_Status_5'])
            Rpay_Status_6 = int(request.form['Rpay_Status_6'])
            Statement_1 = int(request.form['Statement_1'])
            Statement_2 = int(request.form['Statement_2'])
            Statement_3 = int(request.form['Statement_3'])
            Statement_4 = int(request.form['Statement_4'])
            Statement_5 = int(request.form['Statement_5'])
            Statement_6 = int(request.form['Statement_6'])
            Payment_1 = int(request.form['Payment_1'])
            Payment_2 = int(request.form['Payment_2'])
            Payment_3 = int(request.form['Payment_3'])
            Payment_4 = int(request.form['Payment_4'])
            Payment_5 = int(request.form['Payment_5'])
            Payment_6 = int(request.form['Payment_6'])
            
            prediction=model.predict([[CreditAmount,Age,Rpay_Status_1,Rpay_Status_2,Rpay_Status_3,Rpay_Status_4,Rpay_Status_5,Rpay_Status_6,Statement_1,Statement_2,Statement_3,Statement_4,Statement_5,Statement_6,Payment_1,Payment_2,Payment_3,Payment_4,Payment_5,Payment_6,Gender_Male,Gender_Female,Education_Graduate,Education_University,Education_HighSchool,Education_Others,MaritalStatus_Married,MaritalStatus_Single,MaritalStatus_Others]])
            if prediction[0] == 1:
                alert_message = "This account will be defaulted"
            else:
                success_message = "This account will not be defaulted"

            Default_pay = int(prediction[0])
            dbHandler.insertUser(FirstName,LastName,Email,Education,Age,SSN,PhoneNumber,Gender,MaritalStatus,CreditAmount,Rpay_Status_1,Rpay_Status_2,Rpay_Status_3,Rpay_Status_4,Rpay_Status_5,Rpay_Status_6,Statement_1,Statement_2,Statement_3,Statement_4,Statement_5,Statement_6,Payment_1,Payment_2,Payment_3,Payment_4,Payment_5,Payment_6,Default_pay)
    except:
        alert_message = "Please enter relevant information."
    return render_template('webpageupdated.html',alert_message = alert_message, success_message = success_message)
        

if __name__ == "__main__":
    app.run(debug=True)
