import requests
import urllib.parse 


client_id =  '0TA1OMMCO5X0XS3IGPZEALZE1BQKIYMNWRW2XV2OPEWIZPDY'
client_secret = 'HXPPPMBTMZM2PDLIRWVHQ2VJHAIAHIXWK04ESZICOSHP2UMM'
endpoint = 'https://foursquare.com/oauth2/authenticate'
redirect_uri = 'http://localhost:8080/redirect'
query_string={
	'client_id': client_id,
	'response_type': 'code',
	'redirect_uri': redirect_uri
}

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}


req = requests.post(endpoint, params=query_string)
print(req.content) #this just returns the URL from the req above





# redirect_url = parsed_url.split('&')[2]
# final_encoded = redirect_url.split('=')[1]
# final_unencoded = urllib.parse.unquote(final_encoded)
# print(final_unencoded)
# code_get = requests.get(final_unencoded)
# print(code_get.url)