import requests

endpoint = 'https://api.foursquare.com/v2/'
token = 'CWVT1SWOPC1XSEQQPEJCOHOE35N1H1MXAVERZG0PIDHHMYWZ'
version = 20161013
location = "Harlem, New York, NY"
query = "Coffee"
ll = "40.8258195,-73.9544266"

queryString = {
    'oauth_token':token,
    'v':version,
    'near':location,
    'query':query.replace(' ', "%20"),
    #'ll' : ll
}

req = requests.get(endpoint + '/venues/explore?', params=queryString)
print(req.url)
json_data = req.json()
resText = req.content

for value in json_data['response']['groups'][0]:
    print(value['name'])