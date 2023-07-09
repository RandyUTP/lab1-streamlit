import streamlit as st
from PIL import Image
image = Image.open('hidra.png')
st.image(image, caption='',use_column_width=True)

st.title("Test de riesgo Covid-19 :sunglasses:")

html_temp = """
<div style="background-color:#26c5de;padding:0.2 px">
<h2 style="color:white;text-align:left;">Evaluación del nivel de exposición al Covid19: </h2>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)

st.write('**[1] ¿Sales de casa?**')
sales=st.selectbox(label="",options=['Nunca','Algunas veces','Frecuentemente'],index=0,)

st.write('**[2] ¿Has estado últimamente en una zona de riesgo como: trasporte publico,supermercados,tiendas u bancos?**')
publico=st.selectbox(label="",options=['Si','No'],index=0,)

st.write('**[3]¿Cual de estas medidas tomas al salir?**')
medidas=st.multiselect(label="Puedes seleccionar más de una:",options=['Nunca salgo','Mascarilla','Guantes','Lentes','Mameluco','Ducha al regresar'])

st.write('**[4]¿Has estado o crees haber estado en contacto directo con algún contagiado de COVID-19?**')
contacto=st.selectbox(label=" ",options=['Si','No'],index=0,)

st.write('**[5]¿Tienes algún familiar policia, militar, medico, enfermero?**')
familiar=st.selectbox(label="  ",options=['Si','No'],index=0,)
