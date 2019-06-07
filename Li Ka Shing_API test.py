# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:51:45 2019

@author: Dick Sang
"""

import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

params = urllib.parse.urlencode({
            # Request parameters
            'visualFeatures' : 'Faces',
            'details': 'Celebrities',
            'language': 'en'
})

body = "{'url':'https://www.thetimes.co.uk/imageserver/image/methode%2Fsundaytimes%2Fprod%2Fweb%2Fbin%2F7eb13a92-270a-11e9-9ff0-49a5245b8995.jpg?crop=2667%2C1500%2C0%2C0&resize=685'}"

headers = {
            # Request headers
            'Content-Type': 'application/json', # return format
            'Ocp-Apim-Subscription-Key': '99cca76e0c9842ce9457dcb36963119d' # key to call API
}

conn = http.client.HTTPSConnection('eastasia.api.cognitive.microsoft.com')
conn.request("POST", "/vision/v1.0/analyze?%s" %params, body, headers)
response = conn.getresponse()
data = response.read()
data_json = json.loads(data)

name = data_json["categories"][0]["detail"]["celebrities"][0]["name"]
confidence = data_json["categories"][0]["detail"]["celebrities"][0]["confidence"]

print('------------------- testing results -------------------')
print('name: ' + name)
print('confidence: ' + str(confidence))

conn.close()