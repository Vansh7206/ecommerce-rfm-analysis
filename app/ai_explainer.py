import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def explain_result(user_query, result):

    prompt = f"""
You are a business analyst.

User question:
{user_query}

Here is the result:
{result}

Explain the insight clearly in 3-4 lines.
Focus on business meaning.
Do not write code.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"].strip()