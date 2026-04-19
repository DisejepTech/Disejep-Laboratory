import streamlit as st
from PIL import Image
import os

# Operational Configuration
st.set_page_config(page_title="Disejep Laboratory", layout="wide")

# --- VISUAL HEADER (The Bridge) ---
# Forzamos la búsqueda del archivo en el directorio raíz
banner_path = "01 BANNER BUENO DISEJEP.jpg"

if os.path.exists(banner_path):
    header_source = Image.open(banner_path)
    st.image(header_source, use_container_width=True)

# --- CORE INTERFACE ---
st.title("Disejep Laboratory")
st.caption("Registered Trademark: OJ")
st.divider()

# --- DATA INPUT ---
st.write("Source input for deterministic processing:")
input_data = st.file_uploader("Select Source File", type=["jpg", "jpeg", "png", "tiff"], label_visibility="collapsed")

if input_data is not None:
    sample = Image.open(input_data)
    st.image(sample, caption="Input Data Stream", width=600)
    st.info("Source successfully synchronized.")
