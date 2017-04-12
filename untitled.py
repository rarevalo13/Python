import requests
import urllib2
import httplib


client_id = '0TA1OMMCO5X0XS3IGPZEALZE1BQKIYMNWRW2XV2OPEWIZPDY'
client_seceret = 'HXPPPMBTMZM2PDLIRWVHQ2VJHAIAHIXWK04ESZICOSHP2UMM'
redirect_uri = 'http://localhost:8080/redirect'
authenticate_url = 'https://foursquare.com/oauth2/authenticate'

payload = {
	'client_id': client_id,
	'response_type': 'code',
	'redirect_uri': redirect_uri
}

httplib.HTTPConnection.debuglevel = 1
request = urllib2.Requet(authenticate_url)