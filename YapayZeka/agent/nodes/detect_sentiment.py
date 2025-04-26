# agent/nodes/detect_sentiment.py

import requests

class SentimentDetector:
    def __init__(self, model: str = "llama3"):
        self.base_url = "http://localhost:11434/api/generate"
        self.model = model

    def detect(self, question: str) -> str:
        system_prompt = (
            "Sen bir müşteri temsilcisisin. "
            "Kullanıcının mesajındaki duyguyu belirle: "
            "1) Öfkeli, 2) Üzgün, 3) Mutlu, 4) Nötr, 5) Diğer "
            "Sadece bir kelime ile cevap ver (örneğin: Öfkeli, Üzgün, Mutlu, Nötr, Diğer). "
            "Açıklama yapma.\n\n"
            f"Mesaj: {question}\n\nDuygu:"
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
