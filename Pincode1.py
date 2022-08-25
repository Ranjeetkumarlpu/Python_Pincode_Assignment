import requests

import json

ENDPOINT = "https://api.postalpincode.in/pincode/"

pincode = input("enter your pincode:")


requests.get(ENDPOINT+pincode)


response= requests.get(ENDPOINT+pincode)

pincode_information= json.loads(response.text)

print(pincode_information[0]['PostOffice'][0])

necessary_information= pincode_information[0]['PostOffice'][0]

for key, value in necessary_information.items():

    print(f"{key}:{value}")
