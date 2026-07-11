# STEP 1: Ask a question, get an AI answer.

import requests
import os
from dotenv import load_dotenv

load_dotenv()  # this reads your .env file
api_key = os.getenv("ANTHROPIC_API_KEY")

def ask_ai(question):
    response = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        json={
            "model": "claude-sonnet-4-6",
            "max_tokens": 300,
            "messages": [{"role": "user", "content": question}],
        },
    )
    data = response.json()
    return data["content"][0]["text"]

question = input("Ask me anything: ")
answer = ask_ai(question)
print("\nAI says:\n", answer)