# llm_connection/llm_client.py

import requests

class LLMClient:
    def __init__(self, model: str = "llama3"):
        self.base_url = "http://localhost:11434/api/generate"
        self.model = model

    def generate_response(self, prompt: str) -> str:
        system_prompt = "Sen kibar ve yardımsever bir müşteri destek temsilcisisin. Kullanıcıya TÜRKÇE cevap ver."
        full_prompt = f"{system_prompt}\n\nKullanıcının sorusu: {prompt}"

        payload = {
            "model": self.model,
            "prompt": full_prompt,
            "stream": False
        }
        response = requests.post(self.base_url, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["response"].strip()
