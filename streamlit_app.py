import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image



@st.cache
def load_dataset():
    dataset = pd.read_csv('Casos_Anemia_Region_Cusco_2010_2020_Cusco.csv', encoding='latin-1' , sep=';')
    return dataset



plt.figure(figsize=(16,6))
plt.bar(data_nn['PROVINCIA'].unique(),data['PROVINCIA'].value_counts())
plt.title('G')
plt.show()
