"""

This script utilizes an API to create a habit tracking
graph.

This script requires that 'python_dotenv', 'requests' be installed within the Python
environment you are running this script in.

"""

import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv(".env")
PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")
USER_PARAMS = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}


# response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMS)
# print(response.text)

GRAPH_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'
GRAPH_PARAMS = {
    'id': 'graph1',
    'name': 'Coding Graph',
    'unit': 'Hr',
    'type': 'float',
    'color': 'ichou'
}
HEADERS = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_PARAMS, headers=HEADERS)
# print(response.text)

hours_spent_coding = input('How many hours did you spend coding? Give a float number.')

PIXEL_PARAMS = {
    'date': dt.datetime.now().strftime('%Y%m%d'),
    'quantity': hours_spent_coding
}

POST_PIXEL_ENDPOINT = f'https://pixe.la/v1/users/{USERNAME}/graphs/graph1'

response = requests.post(url=POST_PIXEL_ENDPOINT, json=PIXEL_PARAMS, headers=HEADERS)
print(response.text)

# Challenge: Update Yesterdays data point to a new value using a HTTP Put request.
# date_to_change = (dt.datetime.now()-dt.timedelta(days=1)).strftime('%Y%m%d')
# PUT_PIXEL_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/{date_to_change}'
# PUT_PIXEL_PARAMS = {
#     'quantity': hours_spent_coding,
# c
# response = requests.put(url=PUT_PIXEL_ENDPOINT, json=PUT_PIXEL_PARAMS, headers=HEADERS)
# print(response.text)

# Challenge: Delete todays data point using a HTTP Delete request

# DELETE_PIXEL_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/{date_to_change}'
#
# response = requests.delete(url=DELETE_PIXEL_ENDPOINT, headers=HEADERS)
# print(response.text)