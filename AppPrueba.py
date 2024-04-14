import streamlit as st
import pandas as pd
st.title("Busca tu casa")
st.write("Mi nueva APP")
buttonL = st.button("Log in")
buttonI = st.button('Invitado')
if buttonI:
  st.write('Estas son las casas')
if buttonL:  
  correo = st.text_input("Ingresa tu correo")
  password = st.text_input("Ingresa tu contraseña", type="password")
  if st.button("Ingresar"):
    st.write("Tu correo es: ", correo)
    st.write("Tu contraseña es: ", password)
  
