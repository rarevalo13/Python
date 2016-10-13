import requests
from PIL import Image
from io import BytesIO
import os
import os.path
import sys
import pyperclip

#Global Variables, change as necessary 
user = 'YOURUSERDIR'
customer = "THECUSOTMER"
auth_token = 'CUSTOMERAUTHTOKEN'

#Media you wish to download
medias = []
query = {
    'auth_token': auth_token,
    'version' : 'v2.2'
}

create_dir = os.mkdir('/Users/{}'.format(user) + '/downloads/{}'.format(customer))
target_dir = '/Users/{}'.format(user) + '/downloads/{}'.format(customer)
os.chdir(target_dir)

def get_images(media):
    for media in medias:
        url ="https://photorankapi-a.akamaihd.net/media/{}".format(media)  
        response = requests.get(url, params=query)
        json_data = response.json()
        mobileURL = json_data['data']['images']['original']
        photoID = json_data['data']['id']
        date = json_data['data']['date_submitted']
        username = json_data['data']['_embedded']['uploader']['username']
        photosreq = requests.get(mobileURL)
        photo_file = Image.open(BytesIO(photosreq.content))
        photo_file.save(username + '_' + photoID + ".jpeg", 'jpeg')


get_images(medias)

print('ಠ_ಠ DONE!')