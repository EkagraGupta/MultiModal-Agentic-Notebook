import requests
import json

def stub_chat(messages):
    last_user_message = next(
        (m["content"] for m in reversed(messages) if m["role"]=="user"), ""
    )

    return f"[llm]  I read: '{last_user_message}' - dummy right now."

def chat(messages):
    
    try:
        user_text = "\n".join(
            f"{m['role'].capitalize()}: {m['content']}" for m in messages
        )

        payload = {
            "model": "phi3",
            "prompt": user_text,
            "stream": False
        }

        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        return data.get("response", "").strip()
    
    except requests.exceptions.RequestException as e:
        print(f"Ollama http error: {e}")
        return stub_chat(messages)