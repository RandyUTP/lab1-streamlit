import streamlit as st
from PIL import Image 
image = Image.open('hidra.png')
st.image(image)
