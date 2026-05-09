# import json
# person = {
#     "name": "Tisa",
#     "city": "Toronto",
#     "Scores": [98,87,92]
# }

# json.dump(person, open("data.json","w"))
# with open('data.json','r') as f:
#     d= json.load(f)

# print(d["name"]) 
# s = d["Scores"][1]
# print(s)


# # for score in scores:
# #     print(score)


import json
import requests
response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
# print(response.json())

data = response.json()
# print(f"{data["CAD"]["usd"]}")

currencies = ["CAD","GBP","EUR","AUD","INR"]
for cur in currencies:
    print(f"USD -> {data["rates"][cur]}: {cur}")


to_save = {}
for cur in currencies:
    to_save[cur] = data["rates"][cur]

to_save["date"] = data["date"]
json.dump(to_save, open("rates.json","w"))


# for cur in data:
#     print(cur)
