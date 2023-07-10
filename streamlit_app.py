import streamlit as st
import pandas as pd
from PIL import Image

image = Image.open('hidra.png')
st.image(image,use_column_width=True)
