
from ast import Raise
import os
import configparser
import requests
import datetime
import json

class BackgroundCheckAPI():
    '''
    ROOT NODES CHILD NODES POSSIBLE NODE VALUES
        
        #Credentials
        App_ID Records API App ID (Required)
        App_Key Records API App Key (Required)
        Timestamp Current Timestamp (Required)

        #Catalogue
        BACKGROUND Retrieve BACKGROUND Records (Required)

        #Query Parameters
        FirstName Person’s first name (Optional)
        LastName Person’s Last name (Required)
        MiddleName Person’s Middle name (Optional)
        State Person’s State (Optional)
        County Person’s County (Optional)
        City Person’s City (Optional)
        BirthYear Person’s Birth Year (Optional)
        CrimeType
        Crime Type Like Inmate, Released Inmate, Offender etc.
        For all types left this field blank.
        ExactMatch Exact Match (Yes/No) (Optional) Default is Moderated
        '''
    def __init__(self,type="JSON") -> None:
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.format = type
        self.base_url = config[type]["baseUrl"]
        self.session = requests.session()
        self.get_auth()

    def post(self,route,data):
        payload_dict = {
            "credentials" : {
                "App_ID"  : self.app_id,
                "App_Key" : self.app_key,
                "Timestamp" : datetime.datetime.now().timestamp()
            },
            "catalogue" : "BACKGROUND",
            "datatype" : self.format,
            "data" : data
        }

        if self.format == "JSON":
            payload = json.dumps(payload_dict)
        else:
            raise NotImplementedError("Only JSON formate is supported in the api wrapper for now")

        response = self.session.post(self.base_url + route, payload )
        return response

    def get(self,route,data):
        payload = {
            "App_ID"  : self.app_id,
            "App_Key" : self.app_key,
            "Timestamp" : datetime.datetime.now().timestamp(),
            "catalogue" : "BACKGROUND",
            "datatype" : self.format,
        }
        payload.update(data)

        response = self.session.get(self.base_url + route, params=payload)
        return response

    def get_auth(self):
        self.app_id = os.getenv('BCGCHK_APP_ID')
        self.app_key= os.getenv('BCGCHK_APP_KEY')


    def check_by_name(self, last , first = "", middle = "", state= "", county = "", city = "", birth_year = ""):
        '''
            LastName Person’s Last name (Required)
            FirstName Person’s first name (Optional)
            MiddleName Person’s Middle name (Optional)
            State Person’s State (Optional)
            County Person’s County (Optional)
            City Person’s City (Optional)
            BirthYear Person’s Birth Year (Optional)
        '''
        data = {"LastName" : last}
        #if first : 
        data["FirstName"] = first
        #if middle : 
        data["MiddleName"] = middle
        #if state :
        data["State"] = state
        #if county : 
        data["County"] = county
        #if city:
        data["City"] = city
        #if birth_year:
        data["BirthYear"] = birth_year
        
        response = self.get("/", data)
        return response
    



