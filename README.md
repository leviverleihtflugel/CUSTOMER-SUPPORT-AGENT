 Problemin Tanımı ve Projenin Amacı
Günümüzde e-ticaret platformları, hizmet sektörleri ve firmalar her gün binlerce müşteri sorusu ve şikayetiyle karşılaşmaktadır.
Bu taleplerin hızlı, doğru ve kullanıcı odaklı şekilde cevaplanması müşteri memnuniyeti için çok önemlidir.
Ancak bu yoğunluğu yönetmek, insan destek ekipleri için hem zaman alıcı hem de maliyetlidir.
Özellikle basit ve tekrar eden soruların manuel olarak cevaplanması kaynak israfına yol açmaktadır.
Bu bağlamda geliştirilen Customer Support Agent projesi;
•	Kullanıcılardan gelen mesajları anlayarak,
•	Kategorilendirerek,
•	Duygularını analiz ederek,
•	Öncelik sıralaması yaparak,
•	Gerekirse bilgi tabanından veya yapay zekadan hızlı yanıt üreterek,
müşteri destek süreçlerini otomatik, akıllı ve yerel LLM tabanlı bir şekilde yönetmeyi amaçlamaktadır.
Projenin temel hedefi:
•	Müşteri destek süreçlerini hızlandırmak,
•	Hataları azaltmak,
•	Kullanıcı deneyimini geliştirmek,
•	Ve şirketlerin müşteri ilişkileri yönetimini yapay zeka destekli bir sisteme dönüştürmektir.
________________________________________
Programın Ne Yaptığı ve Nasıl Kullanıldığı
Uygulama Streamlit ile oluşturulan bir kullanıcı arayüzü üzerinden çalışır. Kullanıcı metin kutusuna sorun ya da mesajını yazar. Ardından sistem:
1.	Mesajı sınıflandırır (örn. iade, teknik destek, şikayet vs.)
2.	Kullanıcının niyetini (intent) çıkarır.
3.	Duygusal tonu analiz eder.
4.	Öncelik seviyesini belirler.
5.	Gerekirse bilgi tabanında arama yapar.
6.	Eğer bilgi bulunamazsa LLM'den (Llama3 modeli) özgün bir yanıt oluşturur.
7.	Yanıtı özetler.
8.	Tüm bu bilgileri bir log dosyasına kaydeder.
Kullanıcıya ise ekranda şu bilgiler gösterilir:
•	Sınıflandırılan Kategori
•	Belirlenen Amaç
•	Algılanan Duygu
•	Öncelik Seviyesi
•	Verilen Yanıt
•	Cevap Özeti
________________________________________
Programın Çalışma Mantığı ve Düğümlerin Açıklaması
Sistem, bileşen bazlı (node tabanlı) bir mimari ile geliştirilmiştir. Aşağıda her bir düğümün görevi yer almaktadır:
Düğüm	Açıklama
QuestionClassifier	Kullanıcının mesajını kategoriye ayırır (örn. iade, şikayet, bilgi vs.)
IntentExtractor	Mesajın amacını belirler (örn. bilgilendirme, şikayet, teşekkür)
SentimentDetector	Metindeki duygusal tonu (mutlu, öfkeli, üzgün vb.) analiz eder
PriorityScorer	Mesajın önem derecesine göre “Düşük, Orta, Yüksek” puanı atar
KnowledgeBaseSearcher	Bilgi tabanında mesajla eşleşen kayıt varsa bunu yanıt olarak döner
LLMClient	Bilgi tabanında sonuç bulunmazsa, Llama3 modelinden cevap üretir
SummaryGenerator	LLM yanıtlarını kısa özet haline getirir (1-2 cümle)
ConversationLogger	Tüm sonuçları bir JSON dosyasına kaydeder (conversation_logs.json)
Streamlit arayüzü	Kullanıcı girişleri, butonlar ve çıktıların gösterildiği grafik arayüzdür
Toplamda 9 bağımsız düğüm kullanılmıştır.
________________________________________
🌐 Kullanılan Kodların Kaynakları
Proje boyunca kullanılan kodların çoğu tarafımızdan geliştirilmiştir.
Ancak aşağıdaki kaynaklardan yararlanılmıştır:
•	Ollama (Llama3) modeli — Yerel LLM çalıştırma altyapısı
•	Streamlit Resmi Dokümantasyonu – https://docs.streamlit.io
•	Python requests kütüphanesi — https://pypi.org/project/requests/
Tüm LLM istemci çağrıları OpenAI veya Ollama API uyumlu formatta yazılmıştır.
________________________________________
Framework Kullanımı ve Kurulum Bilgisi
Python 3.10+ bilgisayarınızda kurulu olmalıdır.
Gerekli Python paketlerini yüklemek için terminale şunu yazın:
C:\Users\leviv> pip install streamlit requests
Ollama isimli Local LLM çalıştırıcısını kurun ve çalıştırın:
(https://ollama.com/download)
Ollama kurulduktan sonra, terminale şu komut ile Llama3 modelini indirin ve başlatın:
C:\Users\leviv> ollama run llama3
Proje dosyalarını bilgisayarınıza kopyalayın:
(Örneğin masaüstünde YapayZeka adlı bir klasörde)
Terminalde proje klasörüne gidin:
C:\Users\leviv> cd C:\Users\KullaniciAdi\Desktop\YapayZeka
Projeyi çalıştırın:
C:\Users\leviv\YapayZeka> streamlit run streamlit_app.py 
Bu adımlar tamamlandığında, uygulama tarayıcınızda açılacaktır.
Yerel LLM (Llama3) ile çalışan müşteri destek asistanınız kullanıma hazırdır! 🚀
