# agent/nodes/knowledge_base_search.py

class KnowledgeBaseSearcher:
    def __init__(self):
        # Basit bilgi bankası verileri (örnek veriler)
        self.knowledge_base = {
            "kargo ne zaman gelir": "Kargolar genellikle 2-5 iş günü içerisinde teslim edilir.",
            "ürünümü nasıl iade edebilirim": "İade etmek için 14 gün içinde müşteri hizmetlerimize başvurabilirsiniz.",
            "garanti süresi ne kadar": "Tüm ürünlerimizde 2 yıl garanti süresi bulunmaktadır.",
            "ödeme yöntemleri nelerdir": "Kredi kartı, banka kartı ve kapıda ödeme seçeneklerimiz vardır.",
            "siparişimi nasıl iptal edebilirim": "Siparişinizi kargoya verilmeden önce iptal edebilirsiniz, lütfen destek ekibimizle iletişime geçin."
        }

    def search(self, question: str) -> str:
        question = question.lower()
        for keyword, answer in self.knowledge_base.items():
            if keyword in question:
                return answer
        return ""  # Eğer bulunamazsa boş string döner
