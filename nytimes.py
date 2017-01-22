import sys
import requests
import os
import csv
import webbrowser

api_key = '572ed5f65d5945e582f1af8cf3974fb2'
endpoint = 'http://api.nytimes.com/svc/search/v2/articlesearch.json' 
params = {
	'api_key': api_key,
	'q': str(sys.argv[1]).lower(),
	'sort': 'oldest'
}

req = requests.get(endpoint, params=params)
webbrowser.open(req.url)

with open('nyt.csv', 'wb+') as csvfile:
	dict_writer = csv.DictWriter(csvfile, fieldnames=['url', 'source'])
	dict_writer.writeheader()
	dict_writer.writerows(rows)sdfasd
