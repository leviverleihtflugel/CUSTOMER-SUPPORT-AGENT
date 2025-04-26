# agent/nodes/classify_question.py
# -*- coding: utf-8 -*-

import requests

class QuestionClassifier:
    def __init__(self, model: str = "llama3"):
        self.base_url = "http://localhost:11434/api/generate"
        self.model = model

    def classify(self, question: str) -> str:
        prompt = (
            "Sen bir müşteri destek temsilcisisin.\n"
            "Kullanıcının sorusunu aşağıdaki kategorilerden birine sınıflandır:\n"
            "- İade\n"
            "- Teknik destek\n"
            "- Ürün bilgisi\n"
            "- Şikayet\n"
            "- Diğer\n\n"
            "Sadece kategori adını yaz. Ekstra açıklama yapma.\n\n"
            f"Soru: {question}\n\nKategori:"
        )

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(self.base_url, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["response"].strip().lower()
