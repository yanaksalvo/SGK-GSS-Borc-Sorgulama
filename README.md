# SGK-GSS-Bor-Sorgulama

BGX RPA - SGK/GSS SORGULAMA SİSTEMİ KURULUM VE KULLANIM REHBERİ
Bu yazılım, Yapı Kredi İnternet Şubesi üzerinden toplu TC kimlik numarası sorgulaması yapmak ve sonuçları Excel raporuna dönüştürmek için tasarlanmış bir RPA (Robotik Süreç Otomasyonu) sistemidir.

1. ÖN HAZIRLIK (Sadece İlk Sefer İçin)
Sistemin çalışması için bilgisayarınızda Python yüklü olmalıdır.

Python Yükleyin: https://www.python.org/downloads/ adresinden son sürümü indirin. Kurulum sırasında "Add Python to PATH" seçeneğini mutlaka işaretleyin.

Kütüphaneleri Kurun: Klasör içindeyken bir terminal (CMD) açın ve şu komutu yapıştırıp Enter'a basın:
pip install flask selenium pandas openpyxl

2. SİSTEMİN BAŞLATILMASI
Sistem her kullanılacağında aşağıdaki iki adım sırasıyla uygulanmalıdır:

ADIM A: Güvenli Chrome Penceresini Açmak
Banka güvenliğini aşmak ve botun sizin oturumunuza bağlanmasını sağlamak için:

Klavyenizden Windows + R tuşlarına basın.

Açılan kutuya şu komutu yapıştırın ve Tamam deyin:
chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\BGX_Bot_Profil"

Açılan yeni Chrome penceresinde Yapı Kredi İnternet Şubesi'ne giriş yapın.

Ödemeler > SGK / Prim Ödemeleri > GSS Prim yolunu izleyerek TC numarasının yazıldığı sorgulama ekranına kadar gelin ve sayfayı öylece bırakın.

ADIM B: Yazılım Panelini Çalıştırmak

app.py dosyasının olduğu klasörde sağ tıklayıp "Terminalde Aç" (veya CMD) deyin.

Şu komutu yazıp çalıştırın: python app.py

Herhangi bir tarayıcıyı (Chrome, Edge vb.) açın ve adres çubuğuna şunu yazın:
http://127.0.0.1:5000

3. KULLANIM TALİMATI
Açılan BGX RPA panelindeki metin alanına, sorgulamak istediğiniz TC numaralarını alt alta gelecek şekilde yapıştırın.

"Sorgulamayı Başlat" butonuna basın.

Sistem çalışırken banka sekmesine müdahale etmeyin. Canlı monitör üzerinden işlemleri takip edebilirsiniz.

İşlem bittiğinde çıkan "Raporu İndir" butonu ile sonuçları Excel (.xlsx) formatında bilgisayarınıza kaydedebilirsiniz.

Yeni bir liste sorgulamak isterseniz "Yeni İşlem Yap" butonunu kullanabilirsiniz.

⚠️ ÖNEMLİ UYARILAR
Banka Oturumu: Banka oturumunuz zaman aşımına uğrarsa bot hata verebilir. Bu durumda banka sayfasını yenileyip tekrar giriş yapmanız yeterlidir.

Pencere Yönetimi: Botun çalıştığı Chrome penceresini simge durumuna (minimize) küçültmeyin, ekranda görünür kalması hız ve doğruluk açısından önemlidir.

Veri Formatı: TC numaralarının başında veya sonunda boşluk kalmadığından emin olun (Sistem otomatik temizleme yapar ancak manuel kontrol önerilir).

BGX Automation Systems v2.0

py -m pip install flask selenium pandas openpyxl
python -m pip install flask selenium pandas openpyxl
