# agent/nodes/logger.py

import json
from datetime import datetime
import os

class ConversationLogger:
    def __init__(self, log_file='conversation_logs.json'):
        self.log_file = log_file
        # Eğer dosya yoksa boş bir liste oluştur
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False, indent=4)

    def log(self, user_input, category, intent, sentiment, priority, response):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "user_input": user_input,
            "category": category,
            "intent": intent,
            "sentiment": sentiment,
            "priority": priority,
            "response": response
        }

        # Eski kayıtları oku
        with open(self.log_file, 'r', encoding='utf-8') as f:
            logs = json.load(f)

        # Yeni kaydı ekle
        logs.append(entry)

        # Güncellenmiş kayıtları yaz
        with open(self.log_file, 'w', encoding='utf-8') as f:
            json.dump(logs, f, ensure_ascii=False, indent=4)
