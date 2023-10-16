import requests
import json
import time
url = 'https://icanhazdadjoke.com/'
looper =0
question = input("wanna hear some dad jokes? y/n")
if question == "yes":
    looper =5
    while looper > 0:
        response = requests.get(url, headers={'Accept': 'application/json'})
        print(response.status_code, type(response.status_code))
        if response.status_code==200:
            data = json.loads(response.text)
            print(data['joke'])
        time.sleep(2)
        looper -= 1
else:
    print("bruh why")