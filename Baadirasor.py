import streamlit as st
from datetime import datetime
import os

# Sayfa başlığı
st.title("baadira sor")

# Oturum durumu: soru gönderildi mi?
if "soru_gonderildi" not in st.session_state:
    st.session_state.soru_gonderildi = False

# Eğer soru gönderilmediyse:
if not st.session_state.soru_gonderildi:
    isim = st.text_input("İsminizi yazın:")
    soru = st.text_area("Sorunuzu yazın:")

    if st.button("Gönder"):
        if not soru.strip():
            st.warning("Lütfen bir soru yazın.")
        else:
            if not isim.strip():
                isim = "İsimsiz"

            zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            satir = f"[{zaman}] {isim}: {soru.strip()}\n"

            try:
                with open("sorular.txt", "a", encoding="utf-8") as dosya:
                    dosya.write(satir)
                st.success("Sorunuz başarıyla kaydedildi.")
                st.info("baadir uygun gördüğünde size geri dönüş yapacaktır.")
                st.session_state.soru_gonderildi = True
            except Exception as e:
                st.error(f"Hata oluştu: {e}")

# Eğer soru gönderildiyse, sadece mesaj ve yeni soru butonu göster
else:
    st.info("baadir uygun gördüğünde size geri dönüş yapacaktır.")
    if st.button("Yeni Soru Sor"):
        st.session_state.soru_gonderildi = False

# Ayırıcı ve soruları gösterme bölümü
st.markdown("---")
st.subheader("📋 Sorulan Sorular")

if st.button("Sorulan Soruları Göster"):
    try:
        with open("sorular.txt", "r", encoding="utf-8") as dosya:
            icerik = dosya.read()
        st.text_area("Tüm Sorular", value=icerik, height=300)
    except FileNotFoundError:
        st.warning("Henüz hiç soru gönderilmedi.")
