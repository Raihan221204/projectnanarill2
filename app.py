import streamlit as st

st.set_page_config(page_title="WayangAI", layout="centered")

st.title("🎭 Selamat Datang di WayangAI")
st.write("Temukan kisah dan karakter Wayang Punakawan melalui teknologi AI.")
st.markdown("📸 Unggah gambar wayang → 🧠 AI akan mengenali → 📚 Jelajahi ceritanya!")

st.page_link("pages/1_Deteksi_Wayang.py", label="🔍 Deteksi Karakter Wayang", icon="🖼️")
st.page_link("pages/2_Eksplorasi_Karakter.py", label="📖 Eksplorasi Karakter", icon="📚")
