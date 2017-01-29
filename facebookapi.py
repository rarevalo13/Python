import requests

app_id = '1642501269387552'
app_secret = "8150baad063f9553c350528df11e703c"
client_token = 'e878687a7d83f9a74d9afdd641efad6d'
host = 'https://graph.facebook.com'
main_get = '/v2.5/me'

# r = requests.get(host + main_get, auth=('ron.arevalo@hotmail.com', 'un!0ckh0me1'))
# print(r.json())



def get_fb_token(app_id, app_secret):
    payload = {'grant_type': 'client_credentials', 'client_id': app_id, 'client_secret': app_secret}
    file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
    #print file.text #to test what the FB api responded with
    print(file.url)
    result = file.text.split("=")[1]
    #print file.text #to test the TOKEN
    print(result)

get_fb_token(app_id, app_secret)



