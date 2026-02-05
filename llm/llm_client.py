import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_llm(prompt: str, system: str = ""):
    messages = []

    if system:
        messages.append({
            "role": "system",
            "content": system
        })

    messages.append({
        "role": "user",
        "content": prompt
    })

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",   # ← ACTIVE MODEL
            messages=messages,
            temperature=0
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"\n[LLM ERROR] Reason: {e}")
        return '{"steps": []}'
