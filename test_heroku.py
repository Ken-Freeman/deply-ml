#Lets you test app.py

import requests
import json
from test_data import test_data

response = requests.post("https://damp-sands-62687.herokuapp.com/predict", json = {'data': test_data})
## log out the return code and any headers - not required for this problem but useful
print("response code: ", response.status_code, "content length is ", len(response.content))
#print("headers: ", json.dumps(response.headers.__dict__, sort_keys=True, indent=4))

text_response = response.text
print("Good day to you. The prediction for the data is:", text_response)

