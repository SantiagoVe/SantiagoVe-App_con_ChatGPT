import streamlit as st
import pandas as pd
st.title("Busca tu casa")
st.write("Mi nueva APP")
buttonL = st.button("Log in")
if buttonL:
  correo = st.text_input('Ingresa tu correo')
  st.write('Tu correo es ', correo)
