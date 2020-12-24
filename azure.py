import sys
import requests

APP_ID='d565461b-7d3b-48aa-9485-7e9682d0d838'
PASSWORD='-ypf?.4b8U[AkPPi4PdAxufDE6nmZJON'
TENANT_ID='942b80cd-1b14-42a1-8dcf-4b21dece61ba'
SUBSCRIPTION_ID='4f27b38c-ad3f-43d8-a9a3-01182e5e2f9a'
RESOUCE_GROUP='gwengroup'

def get_token():
    data = "grant_type=client_credentials&client_id={}&client_secret={}&resource=https://management.azure.com/".format(APP_ID, PASSWORD)
    url="https://login.microsoftonline.com/{}/oauth2/token".format(TENANT_ID)
    r = requests.post(url, data)
    if r.status_code != 200:
        print(r.status_code)
        return ""
    json = r.json()
    return json['access_token']

token = get_token()
if token == "":
    exit()
headers = {"Authorization": "Bearer {}".format(token)}
url = "https://management.azure.com/subscriptions/{}/providers/Microsoft.Network/virtualWans?api-version=2020-07-01".format(SUBSCRIPTION_ID)
#url = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.Network/networkVirtualApplianceSKUs?api-version=2020-05-01".format(SUBSCRIPTION_ID, RESOUCE_GROUP)
print(url)
r = requests.get(url, headers=headers)

if r.status_code != 200:
    print(r.status_code)
    exit()
resp = r.json()
for entry in resp['value']:
    print(entry['name'])
    print(entry['type'])

