import requests
import json
url = 'https://icanhazdadjoke.com/'

response = requests.get(url, headers={'Accept': 'application/json'})

data = json.loads(response.text)
data = json.loads(response.text)

print(data['joke'])

