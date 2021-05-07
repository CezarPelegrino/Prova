import requests
import json
import numpy as np

url = "https://api.covid19api.com/live/country/brazil/status/confirmed/date/2020-03-21T13:13:30Z"

response = requests.get(url)
storage = response.json()

storage[0]['Deaths']

#print(type(storage))
#print(len(storage))
#print(storage[0])
#print(type(storage[0]))
#print(storage[0]['Deaths'])
#print(type(storage[0]['Deaths']))
#print(storage[0]['Deaths'])
#print(type(storage[0]['Deaths']))
#print(storage[0]['Deaths'])
for item in range(len(storage)):
    mortes = (storage[item]['Deaths'])
    res = [int(x) for x in str(mortes)]
#    dicionario = dict.fromkeys(res,"number")
    print(type(res))


    




















