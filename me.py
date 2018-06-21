from __future__ import print_function
import time
import looker
import os
from looker.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker.ApiAuthApi()
client_id = os.environ['API_ID'] # str | client_id part of API3 Key. (optional)
client_secret = os.environ['API_KEY'] # str | client_secret part of API3 Key. (optional)
base_url = 'https://localhost:19999/api/3.0/'

try:
    # Login
    api_response = api_instance.login(client_id=client_id, client_secret=client_secret)
    #use client to create new api objects
    client = looker.ApiClient(None, 'Authorization', 'token ' + api_response.access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiAuthApi->login: %s\n" % e)

sdk = looker.UserApi(client)

fields = ''

try:
    # Get Current User
    api_response = sdk.me(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->me: %s\n" % e)
