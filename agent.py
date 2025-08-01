import os
from openai import OpenAI 
from dotenv import load_dotenv
from openai import OpenAIError


#loading variables (openAI api key) from the .env file
load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
#print("Loaded key:", os.getenv("OPENAI_API_KEY"))

model = "gpt-3.5-turbo"

def create_summary(content):
    try: 
        #send a prompt to GPT-4
        response = client.chat.completions.create(
            model = model,
            messages = [
                {"role":"system", "content":"You are a  god of summarisation. You are a skilled summarizer. Given a URL, write a clear, fun, and factually accurate summary in 3–5 sentences. End with a light joke related to the topic."},
                {"role": "user", "content":content}
            ]
        )

        result = response.choices[0].message.content.strip()
        return result
    except OpenAIError as e:
        print(f"[ERROR] OpenAI API request failed: {e}")
        return None

def extract_topics(content):
    try:
        response = client.chat.completions.create(
            model = model, 
            messages=[
                {"role":"system", "content":"You are a great topic finder. Provided the text, you will analyse it and return a list of 5 key topics or keywords."},
                {"role": "user", "content": f"List 5 relevant keywords or topics from this text:\n\n{content}"}
            ]
        )
        return response.choices[0].message.content.strip()
    except OpenAIError as e:
        print(f"[ERROR] OpenAI API request failed: {e}")
        return None
