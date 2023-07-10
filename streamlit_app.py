import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
    #muestra el numero de casos por provincia
    st.write("muestra el numero de casos por provincia")
    plt.figure(figsize=(20,10))
    plt.bar(data_nn['PROVINCIA'].unique(),dataset['PROVINCIA'].value_counts())
    plt.title('numeros de caso por provincia')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(plt.show())

    #GRAFICO DE BARRAS DEL PROMEDIO DE LAS EDADES DE LAS PERSONAS CON CASOS DE ANEMIA POR PROVINCIAS
    st.write("GRAFICO DE BARRAS DEL PROMEDIO DE LAS EDADES DE LAS PERSONAS CON CASOS DE ANEMIA POR PROVINCIAS")
    promedio = dataset.groupby('PROVINCIA')['EDAD'].mean()
    plt.figure(figsize=(16,6))
    promedio.plot(kind='bar')
    plt.title('PROMEDIO DE EDAD POR PROVINCIAS')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(plt.show())

    #GRAFICO DE BARRAS DE LA CANTIDAD DE CASOS(Numero de casos con anemia por debajo del indicador de salud) Y NORMAL(Numero de casos en condiciones normales (sin anemia)) POR PROVINCIA
    st.write("GRAFICO DE BARRAS DE LA CANTIDAD DE CASOS(Numero de casos con anemia por debajo del indicador de salud) Y NORMAL(Numero de casos en condiciones normales (sin anemia)) POR PROVINCIA")
    promedio = dataset.groupby('PROVINCIA').agg({'CASOS': 'sum', 'NORMAL': 'sum'})
    plt.figure(figsize=(16,6))
    promedio.plot(kind='bar')
    plt.title('CANTIDAD DE CASOS Y NORMAL POR PROVINCIAS')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(plt.show())

    #GRAFICO DE BARRAS DE LA CANTIDAD DE CASOS(Numero de casos con anemia por debajo del indicador de salud) Y NORMAL(Numero de casos en condiciones normales (sin anemia)) POR AÑO
    st.write("GRAFICO DE BARRAS DE LA CANTIDAD DE CASOS(Numero de casos con anemia por debajo del indicador de salud) Y NORMAL(Numero de casos en condiciones normales (sin anemia)) POR AÑO")
    promedio = data_nn.groupby('ANIO').agg({'CASOS': 'sum', 'NORMAL': 'sum'})
    plt.figure(figsize=(16,6))
    promedio.plot(kind='bar')
    plt.title('CASOS POR AÑO')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(plt.show())

    #GRAFICO DE BARRAS DE CANTIDAD DE CASOS(Numero de casos con anemia por debajo del indicador de salud) Y NORMAL(Numero de casos en condiciones normales (sin anemia)) POR DISTRITO DE LA PROVINCIA DE CHUMBIVILCAS
    st.write("GRAFICO DE BARRAS DE CANTIDAD DE CASOS(Numero de casos con anemia por debajo del indicador de salud) Y NORMAL(Numero de casos en condiciones normales (sin anemia)) POR DISTRITO DE LA PROVINCIA DE CHUMBIVILCAS")
    datos_prov = dataset[dataset['PROVINCIA'] == 'CHUMBIVILCAS']
    promedio = datos_prov.groupby('DISTRITO').agg({'CASOS': 'sum', 'NORMAL': 'sum'})
    plt.figure(figsize=(16,6))
    promedio.plot(kind='bar')
    plt.title('CANTIDAD DE CASOS POR DISTRITO DE LA PROVINCIA DE CHUMBIVILCAS')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(plt.show())

    # Grafico de promedio de casos de anemia por año y provincia
    st.write("Grafico de promedio de casos de anemia por año y provincia")
    provincias = ['ESPINAR', 'CANAS', 'PARURO']
    # Filtrar los datos para las provincias seleccionadas
    data_provincias = dataset[dataset['PROVINCIA'].isin(provincias)]
    # Calcular los promedios de casos de anemia por año y provincia
    promedios_por_anio_provincia = data_provincias.groupby(['ANIO', 'PROVINCIA'])['CASOS'].mean().unstack()
    #Crear el gráfico de barras para los promedios
    plt.figure(figsize=(10, 6))
    promedios_por_anio_provincia.plot(kind='bar')
    plt.title('Promedio de casos de anemia por año y provincia')
    plt.xlabel('Año')
    plt.ylabel('Promedio de casos')
    plt.legend(title='Provincia')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(plt.show())
    #Este código cargará los datos del archivo CSV y luego contará el número de casos de anemia por provincia. Luego, se creará un gráfico de barras que muestra el número de casos en cada provincia.
    #Los nombres de las provincias se mostrarán en el eje x, y el número de casos se mostrará en el eje y. El título del gráfico se establecerá como "Número de casos de anemia por provincia.
    st.write("Grafico de número de casos de anemia por provincia")
    # Obtener el conteo de casos por provincia
    casos_por_provincia = dataset['PROVINCIA'].value_counts()
    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    casos_por_provincia.plot(kind='bar')
    plt.title('Número de casos de anemia por provincia')
    plt.xlabel('Provincia')
    plt.ylabel('Número de casos')
    plt.xticks(rotation=45)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(plt.show())

    #En este ejemplo, estamos contando el número de casos de anemia por departamento y luego creando un gráfico circular que muestra la distribución de casos entre los diferentes departamentos. Los nombres de los departamentos se utilizarán como etiquetas en el gráfico circular.
    st.write("gráfico circular número de casos de anemia por departamento")
    casos_por_departamento = dataset['DEPARTAMENTO'].value_counts()
    # Crear el gráfico circular
    plt.figure(figsize=(8, 8))
    plt.pie(casos_por_departamento, labels=casos_por_departamento.index, autopct='%1.1f%%')
    plt.title('Distribución de casos de anemia por departamento')
    plt.axis('equal')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(plt.show())

    #En este ejemplo, estamos contando el número de casos de anemia por microred y creando un gráfico circular que muestra la distribución de casos entre las microredes
    # Obtener el conteo de casos por microred
    st.write("gráfico circular número de casos de anemia por microred")
    casos_por_microred = data['MICRORED'].value_counts()
    # Crear el gráfico circular
    plt.figure(figsize=(8, 8))
    plt.pie(casos_por_microred, labels=casos_por_microred.index, autopct='%1.1f%%')
    plt.title('Distribución de casos de anemia por microred')
    plt.axis('equal')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(plt.show())



if __name__ == "__main__":
    main()
    
