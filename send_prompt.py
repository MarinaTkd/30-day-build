import os
from openai import OpenAI 
from dotenv import load_dotenv

#loading variables (openAI api key) from the .env file
load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
#print("Loaded key:", os.getenv("OPENAI_API_KEY"))

#send a prompt to GPT-4
response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role":"system", "content":"You are a dev guru, like in satrwars but cooler and with a keyboard"},
        {"role": "user", "content":"Hello, i'm staring my first ever dev project, how can you help me"}
    ]
)

print(response.choices[0].message.content.strip())