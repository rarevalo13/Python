# -*- coding: utf-8 -*-
import requests
from urllib.parse import urlparse
import socketserver


client_id ='88793d16c7434187afde212791fdde5f'
secret = 'ddf04f09f6484146a93559967db32ebb'
redirect_uri = "http://localhost:8080/redirect"
# auth_token = '1788859.88793d1.ca95b1f7b7614bfe800f5c6f8c21364c'
auth_endpoint = 'https://api.instagram.com/oauth/authorize/'
users_endpoint = 'users'
q= 'barevalo23'
scope = 'public_content'

payload = {
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    "response_type": "code",
    'scope': scope
}

r = requests.post(auth_endpoint, params=payload, allow_redirects=True)
print(r.url)


socketserver.BaseRequestHandler()