import os
from openai import OpenAI 
from dotenv import load_dotenv
from openai import OpenAIError
import logging
from openai import OpenAIError, APIConnectionError, RateLimitError



#loading variables (openAI api key) from the .env file
load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
#logging.info("Loaded key:", os.getenv("OPENAI_API_KEY"))

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
    except APIConnectionError as e:
        logging.error(f"[APIConnectionError] Failed to connect to OpenAI: {e}")
    except RateLimitError as e:
        logging.error(f"[RateLimitError] Rate limit exceeded: {e}")
    except OpenAIError as e:
        logging.error(f"[OpenAIError] OpenAI API returned an error: {e}")
    except Exception as e:
        logging.error(f"[Unexpected Error] Something went wrong: {e}")
    

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
        logging.error(f"[OpenAIError] OpenAI API failed while extracting topics: {e}")
    except Exception as e:
        logging.error(f"[Unexpected Error] Failed to extract topics: {e}")