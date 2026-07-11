import requests

def ask_ai(question):
    response = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": "YOUR_API_KEY_HERE",
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
