import requests

url = 'http://localhost:9696/predict'

response = requests.post(url,
                         json={'url': "https://habrastorage.org/webt/rt/d9/dh/rtd9dhsmhwrdezeldzoqgijdg8a.jpeg"}).json()
        