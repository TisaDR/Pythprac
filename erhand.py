import time
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("G_API_KEY")
URL = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

messages  = [ {"role": "system",    "content": "you are a helpful assistant"},
    {"role": "user",      "content": "message 1"},
    {"role": "assistant", "content": "reply 1"},
    {"role": "user",      "content": "message 2"},
    {"role": "assistant", "content": "reply 2"},
]

body = {
   "model" : "openai/gpt-oss-120b",
   "messages":messages,
}

def call_with_retry(URL, headers, max_attempts = 4):
    wait = 1
    for attempt in range(max_attempts):
        try:
          response = requests.post(URL, headers=headers,json = body )
          if response.status_code  == 200:
             data = response.json()
             return data
          elif response.status_code == 429:
             print("rate limited , waiting Xs ")
             time.sleep(wait)
             wait *=2
          else:
             print(f"Unexpected status code:{response.status_code}")
             time.sleep(wait)
             wait *=2
        except requests.exceptions.Timeout:
           print("request times out ")
           time.sleep(wait)
           wait *=2
        except requests.exceptions.ConnectionError:
            print("no internet connection") 
            time.sleep(wait)
            wait *=2  
    print("all attempts failed")
    return None
        
result = call_with_retry(URL, headers)
if result:
    print(result["choices"][0]["message"]["content"])        