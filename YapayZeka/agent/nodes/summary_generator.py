# agent/nodes/summary_generator.py
# -*- coding: utf-8 -*-

import requests

class SummaryGenerator:
    def __init__(self, model: str = "llama3"):
        self.base_url = "http://localhost:11434/api/generate"
        self.model = model

    def summarize(self, text: str) -> str:
        prompt = (
            "Aşağıda verilen müşteri destek yanıtını TÜRKÇE olacak şekilde 1-2 cümlede özetle:\n\n"
            f"Yanıt: {text}\n\n"
            "Özet (Türkçe):"
        )

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(self.base_url, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["response"].strip()
