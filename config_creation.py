import os
import sys
import json
from termcolor import colored
from git import Repo
import webbrowser
from collections import OrderedDict

#adjust your root folder accordingly
root_folder = "/Users/YOURUSER/Olapic/Pinfluencer"

repo = Repo(root_folder)
assert not repo.bare

file_creation_path = root_folder +'/scripts/product_feeds/watchdog/scripts/configs/brands'
import_script_path = root_folder + '/scripts/product_feeds/watchdog/scripts'

#changes to path were file needs to be created
os.chdir(file_creation_path)

#Inputs arguments 
site = str(sys.argv[1]).lower()
header = str(sys.argv[2]).lower()
feed_source = str(sys.argv[3]).lower()
fpath = str(sys.argv[4]).lower()


#creates new branch
git = repo.git
git.checkout('HEAD', b="PF-" + site.split('.')[0])


#chooses either Olapic Standar or Google
if header == 'olapic':
    CONFIG = {
        "site": site,
        "header": header,
        "processor": 'OlapicXmlFeedProcessor',
        "root": 'Products',
        "product": 'Product',
        "ftp_credentials": "olapic",
        feed_source: fpath
    }

    sort_order = ['site', 'header', 'processor', 'root', 'product', 'ftp_credentials', 'ftp_path']



elif header == 'google_feed':
    CONFIG = {
        "site": site,
        "header": header,
        "processor": 'OlapicXmlFeedProcessor',
        "root": 'entry',
        "product": None,
        feed_source: fpath
    }
    sort_order = ['site', 'header', 'processor', 'root', 'product', 'ftp_path']

elif header == 'custom':
	CONFIG ={
		"site": site,
        "header": header,
        "processor": 'OlapicXmlFeedProcessor',
        "root": 'Products',
        "product": 'Product',
        feed_source: fpath
	}
    sort_order = ['site', 'header', 'processor', 'root', 'product', 'feed_url']
else:
    print (colored("¡WARNING! No header found, please review product feed.", 'red'))
    quit()



#orderes dict 
ordered_config = [OrderedDict(sorted(CONFIG.items(), key=lambda k: sort_order.index(k[0])))]

#converts from tuple to dict
CONFIG = json.dumps(ordered_config[0], indent=4, cls=None)


#config file created uses site valriable name
target =  open(site.split('.')[0] + '.py', 'w')
target.write('CONFIG=%s' % str(CONFIG).replace('"product": null,', '"product": None,'))
target.close()

#path changes to run product feed import script
os.chdir(import_script_path)
print(colored("Starting Product Feed Ingestion. This may take a moment.", 'green'))
os.system('python product_feed_ingestor.py %s' % site.split('.')[0])

#Elastic search result opens in webbrowser 
elastic_search_result = webbrowser.open('http://192.168.87.111:9200/' + site +'_alias/_search')