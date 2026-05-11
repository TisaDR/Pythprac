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



system_prompt = "you are a strict assistant"
system = [{"role": "system", "content": system_prompt}]
def get_messages_to_Send(history, system):
   recent = history[-5:]
   output = system + recent
   return output


messages = []
while True:
    user_input = input("You: ")
    messages.append({"role":"user","content":user_input})
    body = {
    "model": "openai/gpt-oss-120b",
    "messages": get_messages_to_Send(messages,system) ,
    "temperature" : 0.1       # the list you've been building
     }
 
    response = requests.post(URL, headers=headers, json=body)
    data = response.json()
    result = data["choices"][0]["message"]["content"]
    print(f"Assistant: {result}")
    messages.append({"role": "assistant", "content": result})
    if user_input.lower() == "quit":
     break

