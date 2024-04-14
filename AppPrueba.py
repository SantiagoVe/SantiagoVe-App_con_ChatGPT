import streamlit as st
import pandas as pd
st.title("Busca tu casa")
st.write("Mi nueva APP")
buttonL = st.button("Log in")
if button:
  correo = st.text_input('Ingresa tu correo')
  password = st.text_input('Ingresa Tu clave')
  st.write('Tu cuenta es: 'correo, password)
