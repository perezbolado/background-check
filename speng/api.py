import configparser
import requests

class SportsEngineAPI():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.format = type
        self.key = config["SportsEngine"]["key"]
        self.base_url = config["SportsEngine"]["baseUrl"]
        self.site_id = config["SportsEngine"]["siteId"]
        self.session = requests.session()
    
    def get_mapping_index(self):
        path = "/mapping_codes"
        params = {"site_id" : self.site_id }
        response = self.get(path, params)
        return response

    def get(self,path,parameters):
        headers = {"Accept": "application/json"}
        response = self.session.get(self.base_url + path, params=parameters, headers=headers)
        return response





    