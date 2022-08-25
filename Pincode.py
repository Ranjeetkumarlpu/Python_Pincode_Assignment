Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import requests

import json

ENDPOINT = "https://api.postalpincode.in/pincode/"

pincode = input("enter your pincode:")
enter your pincode:812006

requests.get(ENDPOINT+pincode)
<Response [200]>

response= requests.get(ENDPOINT+pincode)

pincode_information= json.loads(response.text)

print(pincode_information)

