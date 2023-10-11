import requests
import json
url = 'https://favqs.com/api/qotd'

response = requests.get(url, headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}) 
data = json.loads(response.text)


print(data)

