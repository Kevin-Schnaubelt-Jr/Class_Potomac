import requests
import json

url = 'https://icanhazdadjoke.com/'


response = requests.get(url, headers={'accept': 'application/json'})
data = json.loads(response.text)

print('-------')
print(data['joke'])