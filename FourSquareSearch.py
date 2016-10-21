#-*- coding: utf-8 -*-
import requests

endpoint = 'https://api.foursquare.com/v2/'
token = 'CWVT1SWOPC1XSEQQPEJCOHOE35N1H1MXAVERZG0PIDHHMYWZ'
version = 20161013
location = input("Where are you looking for food? ") 
query = input("What are you craving? ")

queryString = {
    'oauth_token':token,
    'v':version,
    'near':location.replace(' ', '+'),
    'query':query.replace(' ', "%20"),
}

req = requests.get(endpoint + '/venues/explore?', params=queryString)
print(req.url)
json_data = req.json()
resText = req.content

def Explore_Foursquare(query):
    try:

            for value in json_data['response']['groups'][0]['items']:
                print(value['venue']['name'], '—', value['venue']['location']['address'])
    except KeyError:
        for value in json_data['response']['groups'][0]['items']:
            print("There's no Address for ", value['venue']['name'])

Explore_Foursquare(query)