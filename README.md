# 🔒 Güvenlik Sınavı Sistemi

<div align="center">

![Django](https://img.shields.io/badge/Django-5.1.6-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

**Görsel tabanlı güvenlik sınavı uygulaması**

[🚀 Kurulum](#-kurulum) • [📋 Özellikler](#-özellikler) • [🖼️ Ekran Görüntüleri](#️-ekran-görüntüleri) • [🔧 Teknolojiler](#-teknolojiler)

</div>

---

## 📋 Proje Hakkında

Bu proje, güvenlik personeli ve ilgili çalışanlar için tasarlanmış görsel tabanlı bir sınav sistemidir. Kullanıcılar, bagaj ve eşya görsellerini inceleyerek tehdit unsurlarını tanımlamaya yönelik sorulara cevap verirler.

### 🎯 Ana Amaç
- Güvenlik personelinin tehdit unsurlarını tanıma becerilerini test etmek
- Görsel materyallerle interaktif öğrenme deneyimi sunmak
- Sınav sonuçlarını detaylı olarak raporlamak

---

## ✨ Özellikler

### 🔐 Kullanıcı Yönetimi
- **Güvenli Giriş Sistemi**: Kullanıcı adı ve şifre ile kimlik doğrulama
- **Tek Seferlik Sınav**: Her kullanıcı sadece bir kez sınava girebilir
- **Oturum Yönetimi**: Django session tabanlı güvenli oturum kontrolü

### 📝 Sınav Sistemi
- **20 Soruluk Test**: Rastgele seçilen görsel sorular
- **Zaman Sınırı**: Ayarlanabilir sınav süresi (varsayılan: 30 dakika)
- **Çoktan Seçmeli**: A, B, C, D, E şıkları ile cevap seçimi
- **Gerçek Zamanlı Zamanlayıcı**: Kalan süreyi gösteren sayaç

### 🖼️ Görsel İçerik
- **Zengin Görsel Kütüphanesi**: 100+ farklı tehdit unsuru görseli
- **Kategorize Edilmiş İçerik**:
  - 🔫 Ateşli Silahlar
  - 🗡️ Kesici/Delici Aletler
  - 💣 Patlayıcı Düzenekler
  - 🧪 Sıvı Maddeler
  - 🛠️ Tamir Setleri
  - ✅ Tehdit Unsuru Yoktur
  - ❌ Yasaklı Madde Bulunmamaktadır

### 📊 Sonuç Sistemi
- **Anında Değerlendirme**: Sınav bitiminde sonuç gösterimi
- **Detaylı Raporlama**: Her soru için doğru/yanlış durumu
- **Puanlama Sistemi**: Her doğru cevap için 5 puan
- **İstatistikler**: Doğru, yanlış ve boş bırakılan soru sayıları

### 👨‍💼 Admin Paneli
- **Sonuç Takibi**: Tüm kullanıcı sonuçlarını görüntüleme
- **Tarih Bazlı Filtreleme**: Sınav sonuçlarını tarihe göre sıralama
- **Detaylı Analiz**: Kullanıcı performanslarını inceleme

---

## 🖼️ Ekran Görüntüleri

### Giriş Sayfası
Modern ve kullanıcı dostu giriş arayüzü ile sınav bilgileri

### Sınav Sayfası
- Gerçek zamanlı zamanlayıcı
- Görsel soru gösterimi
- Çoktan seçmeli cevap seçenekleri
- İlerleme göstergesi

### Sonuç Sayfası
- Detaylı performans raporu
- Her soru için görsel ve cevap karşılaştırması
- Toplam puan ve istatistikler

---

## 🔧 Teknolojiler

### Backend
- **Django 5.1.6**: Web framework
- **Python 3.8+**: Programlama dili
- **SQLite**: Veritabanı
- **Django ORM**: Veritabanı yönetimi

### Frontend
- **HTML5**: Sayfa yapısı
- **CSS3**: Stil ve animasyonlar
- **JavaScript**: Dinamik zamanlayıcı
- **Responsive Design**: Mobil uyumlu tasarım

### Özellikler
- **Session Management**: Güvenli oturum yönetimi
- **File Upload**: Görsel dosya yönetimi
- **Randomization**: Rastgele soru seçimi
- **Timer System**: Zaman sınırlı sınav

---

## 🚀 Kurulum

### Gereksinimler
- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)
- Git

### Adım 1: Projeyi İndirin
```bash
git clone https://github.com/kullaniciadi/sinav-projesi.git
cd sinav-projesi
```

### Adım 2: Sanal Ortam Oluşturun
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Adım 3: Bağımlılıkları Yükleyin
```bash
pip install django==5.1.6
pip install Pillow  # Görsel işleme için
```

### Adım 4: Veritabanını Hazırlayın
```bash
python manage.py makemigrations
python manage.py migrate
```

### Adım 5: Süper Kullanıcı Oluşturun
```bash
python manage.py createsuperuser
```

### Adım 6: Sunucuyu Başlatın
```bash
python manage.py runserver
```

### Adım 7: Tarayıcıda Açın
```
http://127.0.0.1:8000/
```

---

## 📁 Proje Yapısı

```
sinav_projesi/
├── sinav/                          # Ana uygulama
│   ├── models.py                   # Veritabanı modelleri
│   ├── views.py                    # Görünüm fonksiyonları
│   ├── urls.py                     # URL yapılandırması
│   ├── admin.py                    # Admin paneli
│   └── templates/sinav/            # HTML şablonları
│       ├── giris.html             # Giriş sayfası
│       ├── soru.html              # Sınav sayfası
│       ├── sonuc.html             # Sonuç sayfası
│       └── admin_sonuclar.html    # Admin sonuç sayfası
├── sinav_projesi/                  # Proje ayarları
│   ├── settings.py                # Django ayarları
│   ├── urls.py                    # Ana URL yapılandırması
│   └── wsgi.py                    # WSGI yapılandırması
├── media/                         # Yüklenen dosyalar
│   └── gorseller/                 # Sınav görselleri
├── manage.py                      # Django yönetim aracı
└── db.sqlite3                     # Veritabanı dosyası
```

---

## 🎮 Kullanım

### Kullanıcı Girişi
1. Ana sayfada kullanıcı adı ve şifre girin
2. "SINAVA BAŞLA" butonuna tıklayın
3. Sınav otomatik olarak başlayacaktır

### Sınav Süreci
1. Her soru için bir görsel gösterilir
2. 5 şık arasından doğru cevabı seçin
3. "Sonraki Soru" butonu ile ilerleyin
4. Zamanlayıcıyı takip edin

### Sonuç Görüntüleme
1. Sınav bitiminde sonuç sayfası açılır
2. Detaylı performans raporunu inceleyin
3. Her soru için doğru/yanlış durumunu görün

---

## 🔧 Yapılandırma

### Sınav Ayarları
`sinav/models.py` dosyasında Sinav modelini düzenleyerek:
- Sınav süresini değiştirebilirsiniz
- Sınav başlığını güncelleyebilirsiniz

### Görsel Ekleme
1. Yeni görselleri `media/gorseller/` klasörüne ekleyin
2. Django admin panelinden yeni Soru kaydı oluşturun
3. Görseli yükleyin ve kaydedin

### Kullanıcı Yönetimi
Django admin panelinden:
- Yeni kullanıcılar ekleyebilirsiniz
- Mevcut kullanıcıları düzenleyebilirsiniz
- Sınav sonuçlarını görüntüleyebilirsiniz

---

# Güvenlik ayarları
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```


## 📞 İletişim

- **Geliştirici**: [Adınız]
- **E-posta**: [email@example.com]
- **GitHub**: [github.com/kullaniciadi]

---

<div align="center">

**⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!**

</div>
