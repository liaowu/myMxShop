import requests
import json

def test_post_headers_body_json():
    url = "http://127.0.0.1:8000/goods/"
    
    payload  = {}
    headers= {}
    
    response = requests.request("GET", url, headers=headers, data = payload)

# convert dict to json by json.dumps() for body data. 
    resp = requests.post(url, headers=headers, data=json.dumps(payload,indent=4)) 

    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['url'] == url

    print(response.text.encode('utf8'))

