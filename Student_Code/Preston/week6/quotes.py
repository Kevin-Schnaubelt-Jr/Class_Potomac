import requests
import json
import time
import random
url = 'https://favqs.com/api/qotd/'
looper =0
question = input("wanna hear a quote? y/n")
if question == "yes":
    response = requests.get(url, headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    print(response.status_code, type(response.status_code))
    if response.status_code==200:
        data = json.loads(response.text)
        print(f"'{data['quote']['body']}'")
        print(f"    -{data['quote']['author']}")
    time.sleep(2)
else:
    print("bruh why")

