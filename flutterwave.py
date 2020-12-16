import requests

headerinfo = {'Content-Type': 'application/json',
              'Authorization': 'Bearer FLWSECK_TEST-SANDBOXDEMOKEY-X'}
datainfo = {'account_bank': '044',
    'account_number': '0690000040',
    'amount': 5500,
    'narration': 'Akhlm Pstmn Trnsfr xx007',
    'currency': 'NGN',
    'callback_url': 'https://webhook.site/b3e505b0-fe02-430e-a538-22bbbce8ce0d',
    'debit_currency': 'NGN'}

r = requests.post('https://api.flutterwave.com/v3/transfers', headers=headerinfo,json=datainfo)

print(r.json())
