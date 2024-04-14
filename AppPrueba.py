import streamlit as st
import pandas as pd
st.title("Busca tu casa")
st.write("Mi nueva APP")
buttonL = st.button("Log in")
buttonI = st.button('Invitado')
if buttonI:
  st.write('Estas son las casas')
if buttonL:
  correo = st.text_input("Ingresa por favor tu correo 👇")
  if correo:
    st.write("Tu correo es", correo)
  
