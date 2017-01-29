import requests
from requests.auth import HTTPBasicAuth

main_url = 'https://photorank.atlassian.net'
get_participant = '/rest/servicedeskapi/request/DESK-%s/participant'
get_request = '/rest/servicedeskapi/request/DESK-%d'
issues = [6000, 6001, 6002]


for issue in issues:
    r = requests.get(main_url + get_request % issue, auth=HTTPBasicAuth('ron', 'un!0ckh0me1'))
    if r.json()['reporter']['emailAddress'].split('@')[1] == "olapic.com":
        print(r.json()['reporter']['emailAddress'], r.json()['reporter']['name'])
    else:
        print("Not an Olapic employee or former employee")