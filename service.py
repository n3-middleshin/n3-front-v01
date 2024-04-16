import requests
import json

def post(url:str, data:str, headers:str):
    response = requests.post(url, 
                             data=json.dumps(data), 
                             headers=headers, 
                             cookies={"X-Token":"hahahaha"})
    return response.json() 

def get(url:str, params:str, headers:str):
    response = requests.get(url=url, 
                            params=params,
                            headers=headers, 
                            cookies={"X-Token":"hahahaha"})
    return response.json() 
