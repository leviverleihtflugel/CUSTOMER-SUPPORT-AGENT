# agent/nodes/priority_scoring.py

import requests

class PriorityScorer:
    def __init__(self, model: str = "llama3"):
        self.base_url = "http://localhost:11434/api/generate"
        self.model = model

    def score(self, message: str) -> str:
        system_prompt = (
            "Sen bir müşteri destek temsilcisisin. "
            "Kullanıcının mesajının aciliyetini değerlendir. "
            "Sadece şu üç seviyeden birini tek kelime olarak döndür: Yüksek, Orta, Düşük.\n\n"
            f"Mesaj: {message}\n\nÖncelik:"
        )

        payload = {
            "model": self.model,
            "prompt": system_prompt,
            "stream": False
        }
        response = requests.post(self.base_url, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["response"].strip().lower()
