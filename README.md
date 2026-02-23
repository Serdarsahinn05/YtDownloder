# YouTube Video Downloader 🎥

Python kullanılarak geliştirilmiş, YouTube videolarını yüksek kalitede indirmenizi sağlayan basit ve kullanışlı bir araç. Bu proje, video ve ses dosyalarını işlemek için güçlü `yt-dlp` kütüphanesini kullanır.

## 🚀 Özellikler

* **Yüksek Kalite:** Videoları mevcut en yüksek çözünürlükte indirme.
* **Ses Dönüştürme:** Videoları sadece ses (MP3/M4A) formatında indirme seçeneği.
* **Hızlı ve Güvenilir:** `yt-dlp` altyapısı sayesinde stabil indirme işlemi.
* **Kullanıcı Dostu:** Basit grafik arayüz.

## 🛠️ Gereksinimler

Bu projeyi çalıştırmak için bilgisayarınızda şunların yüklü olması gerekir:

1.  **Python 3.x**: [Python İndir](https://www.python.org/downloads/)
2.  **FFmpeg**: Video ve ses birleştirme işlemleri için zorunludur.

### ⚠️ Önemli: FFmpeg Kurulumu
Bu proje, video ve sesi düzgün işleyebilmek için **FFmpeg** aracına ihtiyaç duyar. FFmpeg proje dosyalarına dahil **değildir**, manuel kurulmalıdır.

**Windows için:**
1.  [FFmpeg.org](https://ffmpeg.org/download.html) adresinden indirin (gyan.dev sürümü önerilir).
2.  İndirdiğiniz arşivden `bin` klasöründeki `ffmpeg.exe` dosyasını çıkarın.(Hala çalışmıyorsa bin klasöründeki diğer exe dosyalarını da aynı klasörün içine atın.)
3.  **Seçenek A (Kolay):** `ffmpeg.exe` dosyasını, bu projenin (`yt_downloader.py`) olduğu klasöre atın.
4.  **Seçenek B (Profesyonel):** FFmpeg'i bilgisayarınızın "Sistem Ortam Değişkenleri"ne (PATH) ekleyin.

## 💻 Kurulum

Projeyi bilgisayarınıza kurmak için aşağıdaki adımları izleyin.

1.  **Projeyi Klonlayın:**
    ```bash
    git clone [https://github.com/Serdarsahinn05/YtDownloader.git](https://github.com/Serdarsahinn05/YtDownloader.git)
    cd YtDownloader
    ```

2.  **Gerekli Kütüphaneleri Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Not: `requirements.txt` dosyası `yt-dlp` kütüphanesini içerir.)*

## ▶️ Kullanım

Kurulum tamamlandıktan sonra programı başlatmak için terminale şu komutu yazın:

```bash
streamlit run yt_downloader.py
```
Program varsayılan tarayıcınızda yeni bir sekme açar.
Program açıldığında YouTube video bağlantısını yapıştırın ve indirme formatını seçerek işlemi başlatın. İndirilen dosyalar proje klasörüne (veya belirlenen downloads klasörüne) kaydedilecektir.

## 📷 Uygulama Arayüzü

<img width="2561" height="1468" alt="yt_downloader" src="https://github.com/user-attachments/assets/79080b87-604a-4f7e-a18e-5f40a9ed923b" />


---
### 📝 Lisans ve Yasal Uyarı
Bu proje sadece eğitim ve kişisel kullanım amaçlıdır. Telif hakkı ile korunan içeriklerin izinsiz indirilmesi ve dağıtılması YouTube Hizmet Koşullarına aykırı olabilir. Kullanıcı, yaptığı işlemlerden kendisi sorumludur.

---
Geliştirici: Serdarsahinn05
---
