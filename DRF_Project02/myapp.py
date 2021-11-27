import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    
    'name' : 'Saif',
    'roll' : 102,
    'city' : 'Khulna',
    
    'name' : 'Abir',
    'roll' : 103,
    'city' : 'Chittagong'
}

json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
data = r.json()
print(data)