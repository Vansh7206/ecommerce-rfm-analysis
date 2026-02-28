import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_intent(user_query):
    prompt = f"""
You are an analytics intent extractor.

Convert the user question into JSON with these keys:

- metric (string)
- aggregation (sum, mean, count)
- group_by (year, state, none)
- last_n_years (integer or null)
- top_n (integer or null)
- sort_order (asc, desc, none)
- comparison (growth, none)

Rules:
- Always return valid JSON.
- If not mentioned, set values to null or "none".
- No explanation.
- No markdown.
- No backticks.

User question:
{user_query}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    raw = response.json()["response"].strip()
    raw = raw.replace("```json", "").replace("```", "").strip()

    return json.loads(raw)