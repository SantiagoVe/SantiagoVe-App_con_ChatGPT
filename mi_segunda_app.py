import streamlit as st

# Título de la app
st.title("Conversor Universal")

# Autor de la app
st.write("Esta app fue elaborada por Santiago Velasquez")

# Diccionario de conversiones
conversiones = {
    "Temperatura": {
        "Celsius a Fahrenheit": lambda c: c * 9/5 + 32,
        "Fahrenheit a Celsius": lambda f: (f - 32) * 5/9,
        "Celsius a Kelvin": lambda c: c + 273.15,
        "Kelvin a Celsius": lambda k: k - 273.15
    },
    "Longitud": {
        "Pies a Metros": lambda pies: pies * 0.3048,
        "Metros a Pies": lambda metros: metros / 0.3048,
        "Pulgadas a Centímetros": lambda pulgadas: pulgadas * 2.54,
        "Centímetros a Pulgadas": lambda cm: cm / 2.54
    },
    # Agregar más categorías y conversiones aquí
}

# Seleccionar categoría y conversión
categoria_seleccionada = st.sidebar.selectbox("Selecciona una categoría", list(conversiones.keys()))
conversion_seleccionada = st.sidebar.selectbox("Selecciona una conversión", list(conversiones[categoria_seleccionada].keys()))

# Pedir entrada al usuario
entrada_usuario = st.number_input("Ingrese el valor a convertir")

# Función para calcular la conversión
def calcular_conversion(entrada, conversion):
    return conversiones[categoria_seleccionada][conversion](entrada)

# Calcular conversión si se presiona el botón "Calcular"
if st.button("Calcular"):
    resultado = calcular_conversion(entrada_usuario, conversion_seleccionada)
    st.write(f"Resultado de la conversión: {resultado}")

# Limpiar resultado si se presiona el botón "Limpiar"
if st.button("Limpiar"):
    st.empty()
