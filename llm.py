import requests

API_KEY = " "
URL = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


messages = [
    {"role": "user", "content": "my name is Tisa and I am learning Python"},
    {"role": "assistant", "content": "Nice to meet you Tisa!"},
    {"role": "user", "content": "what is my name and what am I learning?"}
]


messages = []
while True:
    user_input = input("You: ")
    messages.append({"role":"user","content":user_input})
    body = {
    "model": "openai/gpt-oss-120b",
    "messages": messages        # the list you've been building
     }
 
    response = requests.post(URL, headers=headers, json=body)
    data = response.json()
    result = data["choices"][0]["message"]["content"]
    print(f"Assistant: {result}")
    messages.append({"role": "assistant", "content": result})
    if user_input.lower() == "quit":
     break
    
