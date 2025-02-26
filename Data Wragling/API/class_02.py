import requests

url = "https://api.openweathermap.org/data/2.5/weather"
params = {"q": "Singapore", "appid": "2203972e70f562c3bea789d695129ca6"}

respone = requests.get(url, params)

data = respone.json()

print(data)
