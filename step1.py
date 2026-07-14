# STEP 1: Ask a question, get an AI answer.

import requests
import os
from dotenv import load_dotenv

load_dotenv()  # this reads your .env file
api_key = os.getenv("OPENAI_API_KEY")

def ask_ai(question):
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": "gpt-4o-mini",
            "max_tokens": 300,
            "messages": [{"role": "user", "content": question}],
        },
    )
    data = response.json()
    return data["choices"][0]["message"]["content"]

question = input("Ask me anything: ")
answer = ask_ai(question)
print("\nAI says:\n", answer)