import requests

headerinfo = {'Content-Type': 'application/json',
              'Authorization': 'Bearer FLWSECK_TEST-SANDBOXDEMOKEY-X'}

id = '151513'

r = requests.get('https://api.flutterwave.com/v3/transfers/'+id, headers=headerinfo)


print(r.json())
