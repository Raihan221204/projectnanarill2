import streamlit as st
from utils import punakawan_data

st.set_page_config(page_title="Eksplorasi Karakter", layout="wide")
st.title("📖 Eksplorasi Karakter Wayang Punakawan")

for name, data in punakawan_data.items():
    st.header(name)
    st.image(data["image"], width=200)
    st.write(data["description"])
    st.markdown(f"[📖 Cerita lengkap]({data['link']})")
    st.video(data["video"])
    st.markdown("---")
