import os
from openai import OpenAI 
from dotenv import load_dotenv
from openai import OpenAIError


#loading variables (openAI api key) from the .env file
load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
#print("Loaded key:", os.getenv("OPENAI_API_KEY"))

def create_summary(content):
    try: 
        #send a prompt to GPT-4
        response = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role":"system", "content":"You are a  god of summarisation. You take given text and create brief but fun and humorous summary that remains factually accurate.End every summary with appropriate joke to the topic."},
                {"role": "user", "content":content}
            ]
        )

        result = response.choices[0].message.content.strip()
        return result
    except OpenAIError as e:
        print(f"[ERROR] OpenAI API request failed: {e}")
        return None