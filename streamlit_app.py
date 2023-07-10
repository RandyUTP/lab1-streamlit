import streamlit as st
import pandas as pd
from PIL import Image

image = Image.open('hidra.png')
st.image(image,use_column_width=True)

data=pd.read_csv('/Casos_Anemia_Region_Cusco_2010_2020_Cusco.csv', sep=';')
data.head(5)
