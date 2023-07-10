import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image



# Cargar el dataset y almacenarlo en caché
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

def show_home():
    st.title("Casos de Anemia por Edades entre los años 2010 - 2020 en la Region de Cusco")
    c1,c2=st.columns([3,7])
    c1.image('hidra.png', width=200)
    c2.markdown("## Modelos predictivos con aprendizaje automático")
    c2.markdown("#### Integrantes:")
    c2.write("- Rivera Cumpa Pyerina")

def show_page1():
    st.title("Carga de datos del dataset")
    st.write("Através de la librería pandas se realiza la carga de datos de nuestro dataset")
    
    # Crear un contenedor con un estilo de fondo personalizado
    contenedor = st.container()
    
    # Cargar el dataset
    st.markdown("### Importar librería")
    st.write("import pandas as pd")
    
    st.markdown("### Cargar datos")
    st.write("""@st.cache
    def load_dataset():
    dataset = pd.read_csv('Casos_Anemia_Region_Cusco_2010_2020_Cusco.csv', encoding='latin-1' , sep=';')
    return dataset""")

    st.markdown("### Mostrar datos")
    dataset = load_dataset()
    # Mostrar la tabla con los datos
    st.write(dataset)

def show_page2():
    st.title("Describir datos")
    st.write("Importante para determinar problemas de calidad de datos")
    dataset = load_dataset()
    
    # Mostrar descripción de los datos
    st.markdown("### Descripción del dataset:")
    st.write(dataset.describe())
    st.write("De los resultados obtenemos que: El rango de edades se encuentra entre 0 y 59 años, también que el promedio es de 26,65")
    
    # Obtener el contenido de los datos de las subcategorías de la categoría "provincia"
    subcategorias = dataset["PROVINCIA"].value_counts()
    st.markdown("### Conteo por categoría:")
    st.write("Categoría provincia: ")
    st.write(subcategorias)
    st.write("Los resultados muestran que la moda de la categoría provincia es La Convención")
    
    # Obtener el contenido de los datos de las subcategorías de la categoría "distrito"
    subcategoriaD = dataset["DISTRITO"].value_counts()
    st.write("Categoría distrito: ")
    st.write(subcategoriaD)
    st.write("Los resultados muestran que la moda de la categoría distrito es Echarate")

    st.markdown("### Promedio por cartegoría:")
    # Calcular el promedio de edad por provincia
    promedio_edad_por_provincia = dataset.groupby("PROVINCIA")["EDAD"].mean()
    # Mostrar el promedio de edad por provincia
    st.write("Promedio de edad por provincia:")
    st.write(promedio_edad_por_provincia)
    st.write("De los resultados obtenidos se puede observar que los promedios de edad por provincia se encuentran en un rango de 20 y 30 años")

def show_page3():
    st.title("Visualizar datos: ")
    dataset = load_dataset()

    st.write("Los gráficos presentados a continuación tienen el objetivo de mostrar pictoricamente los datos que se tienen en el dataset para una mejor comprensión")
     # Calcular el promedio de edad por provincia
    st.markdown("### Gráficos de barras:")
    st.write("Gráfico de barras del promedio de edad por provincia de los pacientes con anemia en Cusco:")
    promedio_EP = dataset.groupby('PROVINCIA')['EDAD'].mean()
    st.bar_chart(promedio_EP)
    
    # Conteo de los datos por provincia
    st.write("Gráfico de barras del número de casos de anemia por provincia:")
    conteo = dataset["PROVINCIA"].value_counts()
    st.bar_chart(conteo)

    st.write("Gráfico de barras del promedio de casos de anemia por año y provincia")
    # Seleccionar las provincias a comparar
    provincias = ['ESPINAR', 'CANAS', 'PARURO']
    # Filtrar los datos para las provincias seleccionadas
    data_provincias = dataset[dataset['PROVINCIA'].isin(provincias)]
    # Calcular los promedios de casos de anemia por año y provincia
    promedios_por_anio_provincia = data_provincias.groupby(['ANIO', 'PROVINCIA'])['CASOS'].mean().unstack()
    # Mostrar el gráfico de barras
    st.bar_chart(promedios_por_anio_provincia)

    st.markdown("### Gráficos de líneas:")
    st.write("Gráfico de la evolución de casos de anemia por provincia")
    # Seleccionar las provincias a comparar
    provincias = ['CUSCO', 'CALCA', 'ANTA']
    # Filtrar los datos para las provincias seleccionadas
    data_provincias = dataset[dataset['PROVINCIA'].isin(provincias)]
    # Agrupar los datos por año y provincia y calcular el total de casos por año
    casos_por_anio_provincia = data_provincias.groupby(['ANIO', 'PROVINCIA'])['CASOS'].sum().unstack()
    # Mostrar el gráfico de líneas múltiples en un solo gráfico
    for provincia in provincias:
        st.line_chart(casos_por_anio_provincia[provincia])
    #mostrar datos 
      data_nn =dataset.dropna(subset=['PROVINCIA', 'DISTRITO'])
      st.write(data_nn.isnull().sum())

if __name__ == "__main__":
    main()
    
