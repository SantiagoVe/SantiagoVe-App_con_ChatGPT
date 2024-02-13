import streamlit as st

# Título de la app
st.title("Mi primera app")

# Autor de la app
st.write("Esta app fue elaborada por Santiago Velasquez")

# Preguntar el nombre al usuario
nombre_usuario = st.text_input("Por favor, ingresa tu nombre")

# Imprimir mensaje de bienvenida si se proporciona un nombre
if nombre_usuario:
    if nombre_usuario == "Angie":
        st.write("¡¿Ah?! Eres Angie? Te amo mucho mi linda.")
    else:
        st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")
