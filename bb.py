# create a application that will tell me the sea level at a given location
# using the google maps api

import requests
import json
import os
import sys
import time
import datetime
import pytz
import math
import argparse
import re
import logging
import logging.handlers
import traceback
import urllib
import socket
import subprocess
import signal
import threading
import random
import string
import time
import datetime
import pytz
import math
import argparse
import requests

# set up logging
logger = logging.getLogger('bb')
logger.setLevel(logging.DEBUG)
log_file = 'bb.log'
handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=1000000, backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# set up the argument parser
parser = argparse.ArgumentParser(description='Get the sea level at a given location')
parser.add_argument('location', help='The location to get the sea level for')
parser.add_argument('--api_key', help='The google maps api key')
args = parser.parse_args(['Dublin', '--api_key', 'AIzaSyC16rGFEopkR67fedMT6EjFdJoQAH7SDnU'])  # Replace 'New York' with the desired location and 'YOUR_API_KEY' with your actual API key
location = args.location


# set up the google maps api key
api_key = args.api_key
if api_key is None:
    api_key = os.environ.get('GOOGLE_MAPS_API_KEY')
    
    if api_key is None:
        logger.error('No google maps api key provided')
        sys.exit(1)

# set up the location
location = args.location

# get the latitude and longitude of the location
url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + location + '&key=' + api_key
response = requests.get(url)
data = response.json()

if 'results' in data and len(data['results']) > 0:
    lat = data['results'][0]['geometry']['location']['lat']
    lng = data['results'][0]['geometry']['location']['lng']

    # get the sea level at the location
    url = 'https://maps.googleapis.com/maps/api/elevation/json?locations=' + str(lat) + ',' + str(lng) + '&key=' + api_key
    response = requests.get(url)
    data = response.json()

    if 'results' in data and len(data['results']) > 0:
        sea_level = data['results'][0]['elevation']
        print('The sea level at ' + location + ' is ' + str(sea_level) + ' meters')
        logger.info('The sea level at ' + location + ' is ' + str(sea_level) + ' meters')
    else:
        logger.error('No results found for the location')
else:
    logger.error('No results found for the location')



