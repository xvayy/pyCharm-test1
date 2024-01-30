import requests
import json
import time

url = 'https://api.binance.com/api/v3/ticker/price'

prices = []
for i in range(30):
    response = requests.get(url, params={'symbol': 'BTCUSDT'})
    price = float(response.json()['price'])
    prices.append(price)
    time.sleep(1)

print(prices)
print(len(prices))
print(max(prices))
print(min(prices))