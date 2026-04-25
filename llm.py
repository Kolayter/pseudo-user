from ollama import Client
from dotenv import load_dotenv
import os

from config.settings import LLM_MODEL, LLM_OPTIONS
load_dotenv()
SERVER_IP = os.getenv("SERVER_IP")
SERVER_IP_LOCAL = os.getenv("SERVER_IP_LOCAL")

client = Client(host=SERVER_IP_LOCAL)

def TextToAI(messages, llm=LLM_MODEL, options=LLM_OPTIONS):
    response = client.chat(model=llm, messages=messages, options=options)
    return response['message']['content']