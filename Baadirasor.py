import streamlit as st
from datetime import datetime

st.title("Soru Gönderme Uygulaması")

isim = st.text_input("İsminizi yazın:")
soru = st.text_area("Sorunuzu yazın:")

if st.button("Gönder"):
    if not soru.strip():
        st.warning("Lütfen bir soru yazın.")
    else:
        if not isim.strip():
            isim = "İsimsiz"

        try:
            zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            satir = f"[{zaman}] {isim}: {soru.strip()}\n"

            with open("sorular.txt", "a", encoding="utf-8") as dosya:
                dosya.write(satir)

            st.success("Sorunuz başarıyla kaydedildi.")
        except Exception as e:
            st.error(f"Hata oluştu: {e}")
