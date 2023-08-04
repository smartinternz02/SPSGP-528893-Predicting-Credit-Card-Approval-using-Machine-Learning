# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 15:11:26 2021

@author: HP
"""
# importing the necessary dependencies
from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import os


import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "5LTSIhnTIu25ecqNupdDLYO_U4AIBS8jTHfttjKe-Ekt"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app=Flask(_name_)# initializing a flask app

@app.route('/')# route to display the home page
def home():
    return render_template('index.html') #rendering the home page
@app.route('/Prediction',methods=['POST','GET'])
def prediction(): # route which will take you to the prediction page
    return render_template('index1.html')
@app.route('/Home',methods=['POST','GET'])
def my_home():
    return render_template('index.html')

@app.route('/predict',methods=["POST","GET"])# route to show the predictions in a web UI
def predict():
    #  reading the inputs given by the user
    input_feature=[float(x) for x in request.form.values() ]  
   
    feature_name=["CODE_GENDER","FLAG_OWN_CAR","FLAG_OWN_REALTY","AMT_INCOME_TOTAL","NAME_INCOME_TYPE","NAME_EDUCATION_TYPE","NAME_FAMILY_STATUS","NAME_HOUSING_TYPE","DAYS_BIRTH","DAYS_EMPLOYED","CNT_FAM_MEMBERS","paid_off","#_of_pastdues","no_loan"]
    
    payload_scoring = {"input_data":[{"fields":feature_name,"values":[input_feature]}]}

# NOTE: manually define and pass the array(s) of values to be scored in the next line

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/61764cb9-377a-4bc2-b88b-0220de0c551f/predictions?version=2021-12-13', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    
    print("Scoring response")
    pred= response_scoring.json()
    print(pred)
    
    output = pred['predictions'][0]['values'][0][0]
    print(output)
    
    if output==0:
        prediction = "Eligible"
    else:
        prediction = "Not Eligible"
    
    
    #prediction="Prediction is:"+str(predic)
    
     # showing the prediction results in a UI
    return render_template("result.html",prediction=prediction[0:])
if _name=="__main_":
    
    # app.run(host='0.0.0.0', port=8000,debug=True)    # running the app
    port=int(os.environ.get('PORT',5000))
    app.run(port=port,debug=False,use_reloader=False)