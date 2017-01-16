import sys
import requests
import os
import csv 

api_key = '572ed5f65d5945e582f1af8cf3974fb2'
endpoint = 'http://api.nytimes.com/svc/search/v2/articlesearch.json'
params = {
	'api_key': api_key,
	'q' : str(sys.argv[1]).lower(),
	'sort' : 'oldest'
}

req = requests.get(endpoint, params=params)
print(req);