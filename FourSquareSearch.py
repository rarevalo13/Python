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
    #'near':location,
    'query':query.replace(' ', "%20"),
    #'ll' : ll
    'nearGeoId':672493
}

req = requests.get(endpoint + '/venues/search?', params=queryString)
print(req.url)
json_data = req.json()
resText = req.content

for item in json_data:
    print(json_data['response']['venues'][0]['location'])