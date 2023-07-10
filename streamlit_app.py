import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image



@st.cache
def load_dataset():
    dataset = pd.read_csv('Casos_Anemia_Region_Cusco_2010_2020_Cusco.csv', encoding='latin-1' , sep=';')
    return dataset
def main():
    # Configurar la barra de navegación
    st.sidebar.title("Navegación")
    pages = {
        "Inicio": show_home,
        "Cargar": show_page1,
        "Describir": show_page2,
        "Visualizar": show_page3
    }
    page = st.sidebar.selectbox("Ir a", tuple(pages.keys()))

    # Mostrar la página seleccionada
    pages[page]()
def  carga():
    dataset = load_dataset()
    data_nn =dataset.dropna(subset=['PROVINCIA', 'DISTRITO'])
    st.write(data_nn)
    
