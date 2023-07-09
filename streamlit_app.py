import streamlit as st
from PIL import Image
image = Image.open('hidra.png')
st.image(image, caption='',use_column_width=True)

st.title("Test de riesgo Covid-19 :sunglasses:")
