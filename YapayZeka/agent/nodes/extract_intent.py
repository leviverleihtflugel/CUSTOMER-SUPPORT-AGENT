# agent/nodes/extract_intent.py

import requests

class IntentExtractor:
    def __init__(self, model: str = "llama3"):
        self.base_url = "http://localhost:11434/api/generate"
        self.model = model

    def extract(self, question: str) -> str:
        system_prompt = (
            "Sen bir müşteri destek temsilcisisin. "
            "Kullanıcının sorusuna bakarak amacı belirle: "
            "1) İade, 2) Ürün değişimi, 3) Bilgi alma, 4) Şikayet, 5) Diğer. "
            "Sadece bir kelime ile cevap ver (örneğin: İade, Değişim, Bilgi, Şikayet, Diğer). "
            "Açıklama yapma.\n\n"
            f"Soru: {question}\n\nAmaç:"
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
