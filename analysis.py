import pandas as pd
import matplotlib.pyplot as plt
import requests
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("G_API_key")
URL = "https://api.groq.com/openai/v1/chat/completions"


headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


df = pd.read_csv('symbols_valid_meta.csv')
print(df.head())
print(df.columns.tolist())
print(df.shape) 
print(df["ETF"].value_counts())
print(df["Listing Exchange"].value_counts())
print(df["Financial Status"].value_counts())

etfs = df[df["ETF"] == "Y"]
print(etfs.shape)

deficient = df[df["Financial Status"] == "D"]
print(deficient[["Symbol"]])

etfs  = df[df["ETF"] == 'Y']
print(etfs.shape)

deficient = df[df["Financial Status"] == "D"]
print(deficient[["Symbol","Security Name","Financial Status"]].head(10))

clean = df[df["Test Issue"] == "N"]
print(clean.shape)

grouped = df.groupby("Listing Exchange")["Symbol"].count()
print(grouped)

# grouped.plot(kind="bar")
# plt.title("Securities per Exchange")
# plt.xlabel("Exchange")
# plt.ylabel("Count")
# plt.tight_layout()
# plt.show()

safe_stocks = df[(df["Test Issue"] == "N") &
                 (df["Financial Status"] == "N") &
                  (df["Nasdaq Traded"] == "Y") &
                  (df["ETF"] == "N")
]

print(f"Safe coded to show users: {len(safe_stocks)}")

etfs_only = df[df["ETF"] == "Y"]
per_exchange = etfs_only.groupby("Listing Exchange")["Symbol"].count()
print(per_exchange)

deficient = df[df["Financial Status"] == "D"]
total = df.shape[0]
percentage = (len(deficient)/total) * 100
print(percentage)

fig, ax = plt.subplots(figsize=(10, 6))

per_exchange.plot(kind="bar", ax=ax, color="steelblue", edgecolor="black")

# plt.title("ETFs per Exchange", fontsize=16, fontweight="bold")
# plt.xlabel("Exchange", fontsize=12)
# plt.ylabel("Number of ETFs", fontsize=12)
# plt.xticks(rotation=0)
# plt.tight_layout()
# plt.show()

#ETF vs Stocksplit

# df["ETF"].value_counts().plot(kind="bar")
# plt.title("ETFs vs Stocks on NASDAQ")
# plt.xlabel("ETF (Y = Fund, N = Stock)")
# plt.ylabel("Count")
# plt.tight_layout()
# plt.show()

#Financial Health breakdown
# df["Financial Status"].value_counts().plot(kind="bar")
# plt.title("Financial Health of NASDAQ Listings")
# plt.xlabel("Status (N=Normal, D=Deficient, E=Delinquent, H=Suspended)")
# plt.ylabel("Count")
# plt.tight_layout()
# plt.show()

summary = f"""
NASDAQ Dataset Summary:
Total_securites: {total} 
safe stocks :{len(safe_stocks)}
Deficient Companies:{len(deficient)}
percentage deficinet :{percentage}
Total ETFs:{len(etfs_only)}
Exchange with most ETfs:{per_exchange.idxmax()}
"""   
print(summary)

messages = [
    {"role": "user", "content": f"Here is a summary of NASDAQ data: {summary} Please interpret this in plain English for a non-technical investor."}
]

body = {
    "model": "openai/gpt-oss-120b",
    "messages": messages
}



response = requests.post(URL, headers=headers, json=body)
data = response.json()
# print(data)
result = data["choices"][0]["message"]["content"]
print(f"AI Interpretation:\n{result}")