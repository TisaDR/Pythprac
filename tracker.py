import requests
print(requests)
import time
time.sleep(1)

response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true")
print(response)

print(response.status_code)
print(response.text)

data = response.json()
print(data)
print(type(data))

print(data["bitcoin"]["usd"])
price = data["bitcoin"]["usd"]
print(f"Bitcoin is ${price}")
# price = data["ethereum"]["usd"]
# print(f"Ethereum is ${price}")

for coin in data:
   change = data[coin].get("usd_24h_change", 0)
   price = data[coin]["usd"]
   if change > 0:
      print(f"{coin}  ${price:.2f}   ▲ +{change:>10.2f}%")
   else:
      print(f"{coin}  ${price:.2f}   ▼ {change:>10.2f}%")
   biggest_coin = ""
   biggest_change = 0
   if change > biggest_change:
      biggest_change = change
      biggest_coin = coin

print(f"Biggest gainer: {biggest_coin} +{biggest_change:.2f}%")

    
   


