#!/usr/bin/python3
#
#
####################################################

import os
import requests
import sys

from argparse import ArgumentParser

parser = ArgumentParser(description='Get the current weather information for your zipcode')
parser.add_argument('zip', help='zip/postal code to get weather for')
parser.add_argument('--country', default='us', help='country zip/postal belongs to, default is "us"')

args = parser.parse_args()
api_key = "a0d58d2bcb5aea1de3a7f208bd2435d5"

####################################################
##api_key = os.getenv("OWM_API_KEY")


if not api_key:
    print("Error: no 'OWM_API_KEY' provided")
    sys.exit(1)

url = f"http://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&appid={api_key}"

res = requests.get(url)

if res.status_code != 200:
    print(f"Error talking to weather provider: {res.status_code}")
    sys.exit(1)

print(res.json())

####################################################
###########################