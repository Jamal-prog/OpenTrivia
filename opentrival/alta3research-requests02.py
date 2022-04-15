#!/usr/bin/env python3
import requests
from pprint import pprint

# creates url to local host for machine
URL= "https://aux1-f06b12c4-f620-481d-bf52-a1e5094fd92f.live.alta3.com/"

#turn request to json
resp= requests.get(URL).json()

pprint(resp)
