import streamlit as st
from utils import predict_wayang
from PIL import Image

st.set_page_config(page_title="Deteksi Wayang", layout="centered")

st.title("🔍 Deteksi Karakter Wayang")

uploaded_file = st.file_uploader("Unggah gambar karakter Wayang Punakawan", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar yang Diupload", use_column_width=True)

    with st.spinner("Mendeteksi karakter..."):
        result = predict_wayang(uploaded_file)

    st.success(f"Ini adalah {result['name']}!")
    st.image(result["image"], caption=result["name"])
    st.write(result["description"])
    st.markdown(f"[📖 Baca Cerita]({result['link']})")

    st.video(result["video"])
