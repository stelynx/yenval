import requests
import os

data = ''
with open('./values.json') as f:
    data = f.read()

response = requests.get('https://api.exchangeratesapi.io/v1/latest',
                        params={'access_key': os.environ['ERA_ACCESS_KEY'], 'base': 'EUR', 'symbols': 'JPY'})

if (response.status_code) == 200:
    data = str(response.json()['rates']['JPY'])

with open('./values.json', 'w') as f:
    f.write(data)
