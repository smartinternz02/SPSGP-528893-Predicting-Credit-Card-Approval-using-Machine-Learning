# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 15:56:48 2021

@author: HP
"""

import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "5LTSIhnTIu25ecqNupdDLYO_U4AIBS8jTHfttjKe-Ekt"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": ["CODE_GENDER","FLAG_OWN_CAR","FLAG_OWN_REALTY","AMT_INCOME_TOTAL","NAME_INCOME_TYPE","NAME_EDUCATION_TYPE","NAME_FAMILY_STATUS","NAME_HOUSING_TYPE","DAYS_BIRTH","DAYS_EMPLOYED","CNT_FAM_MEMBERS","paid_off","#_of_pastdues","no_loan"], "values": [[1,1,1,112500.0,2,2,0,0,58.832877,-3.106849,2.0,7,7,16]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/61764cb9-377a-4bc2-b88b-0220de0c551f/predictions?version=2021-12-13', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
