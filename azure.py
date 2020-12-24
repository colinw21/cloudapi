import sys
import requests
import config

#APP_ID=''
#PASSWORD=''
#TENANT_ID=''
#SUBSCRIPTION_ID=''
#RESOUCE_GROUP=''

def get_token():
    data = "grant_type=client_credentials&client_id={}&client_secret={}&resource=https://management.azure.com/".format(config.APP_ID, config.PASSWORD)
    url="https://login.microsoftonline.com/{}/oauth2/token".format(config.TENANT_ID)
    r = requests.post(url, data)
    if r.status_code != 200:
        print("token error:" + r.status_code)
        return ""
    json = r.json()
    return json['access_token']

token = get_token()
if token == "":
    exit()
headers = {"Authorization": "Bearer {}".format(token)}
url = "https://management.azure.com/subscriptions/{}/providers/Microsoft.Network/virtualWans?api-version=2020-07-01".format(config.SUBSCRIPTION_ID)
#url = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.Network/networkVirtualApplianceSKUs?api-version=2020-05-01".format(config.SUBSCRIPTION_ID, config.RESOUCE_GROUP)
print(url)
r = requests.get(url, headers=headers)

if r.status_code != 200:
    print(r.status_code)
    exit()
resp = r.json()
for entry in resp['value']:
    print(entry['name'])
    print(entry['type'])

