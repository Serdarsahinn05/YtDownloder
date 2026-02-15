import streamlit as st
import yt_dlp
import os
import uuid
import shutil

st.title('Youtube Video Downloader')

# --- 1. AYARLAR: FFmpeg ve Klasör Yolları ---
current_dir = os.path.dirname(os.path.abspath(__file__))
ffmpeg_path = os.path.join(current_dir, 'ffmpeg.exe')

# FFmpeg kontrolü
if not os.path.exists(ffmpeg_path):
    st.error("🚨 ffmpeg.exe bulunamadı! Lütfen proje klasörüne atın.")
    st.stop()
# ---------------------------------------------

url = st.text_input('YouTube Linkini Buraya Yapıştır')
format_secim = st.selectbox("Format Seçin", ["Video (MP4)", "Ses (MP3)"])

if st.button('Videoyu Hazırla'):
    if url:
        # Her indirme için rastgele boş bir klasör yarat
        unique_id = str(uuid.uuid4())
        temp_dir = os.path.join(current_dir, f"temp_{unique_id}")

        # Klasörü oluştur (Varsa temizle)
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.makedirs(temp_dir)

        try:
            with st.spinner('İndiriliyor...'):

                # Dosya adını basit tutuyoruz, karmaşık karakterleri yt-dlp halletsin
                output_template = os.path.join(temp_dir, '%(title)s.%(ext)s')

                ydl_opts = {
                    'ffmpeg_location': current_dir,
                    'outtmpl': output_template,
                    'quiet': True,
                    'nocheckcertificate': True,
                    'ignoreerrors': True,
                    'no_warnings': True,
                    # Hata oluşursa durma, devam et
                    'ignore_no_formats_error': True,
                }

                if format_secim == "Ses (MP3)":
                    ydl_opts.update({
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
                    })
                else:
                    ydl_opts.update({
                        # En garantili format seçimi (Sesi ve videoyu ayrı indirip birleştirir)
                        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                    })

                # --- İNDİRME İŞLEMİ ---
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

                # --- KRİTİK DEĞİŞİKLİK: DOSYAYI ARAMA ---
                # Dosya adını tahmin etmiyoruz. Klasörün içine bakıyoruz.
                # Klasörde ne varsa bizim dosyamız odur.
                files_in_dir = os.listdir(temp_dir)

                if files_in_dir:
                    # Klasördeki ilk dosyayı al (Zaten tek dosya var)
                    found_file = files_in_dir[0]
                    full_file_path = os.path.join(temp_dir, found_file)

                    st.success(f"Dosya Bulundu: {found_file}")

                    # Dosyayı okuyup butona ver
                    with open(full_file_path, "rb") as f:
                        file_bytes = f.read()

                    st.download_button(
                        label="⬇️ İndir",
                        data=file_bytes,
                        file_name=found_file,
                        mime="audio/mpeg" if format_secim == "Ses (MP3)" else "video/mp4"
                    )
                else:
                    st.error("İndirme tamamlandı görünüyor ama klasör boş. YouTube engeli olabilir.")

        except Exception as e:
            st.error(f"Beklenmeyen bir hata: {e}")

        finally:
            # Temizlik
            if os.path.exists(temp_dir):
                try:
                    # Streamlit dosyayı RAM'e aldıktan sonra klasörü silebiliriz
                    shutil.rmtree(temp_dir, ignore_errors=True)
                except:
                    pass
    else:
        st.warning("Link girin.")