# -*- coding: utf-8 -*-
import requests
import oauth2 as oauth
from urllib.parse import urlparse
from instagram.client import InstagramAPI

client_id ='88793d16c7434187afde212791fdde5f'
secret = 'ddf04f09f6484146a93559967db32ebb'
auth_token = '1788859.88793d1.ca95b1f7b7614bfe800f5c6f8c21364c'
endpoint = 'users'
q= 'barevalo23'

url = 'https://api.instagram.com/v1/' + endpoint + '/search/?access_token=' + auth_token + '&q=' +q
req = requests.get(url)
print(req.json())



# access_token = auth_token
# client_secret = secret
# api = InstagramAPI(access_token=access_token, client_secret=client_secret)
# print(api.user_liked_media())