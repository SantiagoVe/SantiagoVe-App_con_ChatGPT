import streamlit as st

# Título de la app
st.title("Conversor Universal")

# Autor de la app
st.write("Esta app fue elaborada por Santiago Velasquez")

# Categorías de conversiones
categorias = {
    "Temperatura": ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"],
    "Longitud": ["Pies a Metros", "Metros a Pies", "Pulgadas a Centímetros", "Centímetros a Pulgadas"],
    "Peso/Masa": ["Libras a Kilogramos", "Kilogramos a Libras", "Onzas a Gramos", "Gramos a Onzas"],
    "Volumen": ["Galones a Litros", "Litros a Galones", "Pulgadas cúbicas a Centímetros cúbicos", "Centímetros cúbicos a Pulgadas cúbicas"],
    "Tiempo": ["Horas a Minutos", "Minutos a Segundos", "Días a Horas", "Semanas a Días"],
    "Velocidad": ["Millas por hora a Kilómetros por hora", "Kilómetros por hora a Metros por segundo", "Nudos a Millas por hora", "Metros por segundo a Pies por segundo"],
    "Área": ["Metros cuadrados a Pies cuadrados", "Pies cuadrados a Metros cuadrados", "Kilómetros cuadrados a Millas cuadradas", "Millas cuadradas a Kilómetros cuadrados"],
    "Energía": ["Julios a Calorías", "Calorías a Kilojulios", "Kilovatios-hora a Megajulios", "Megajulios a Kilovatios-hora"],
    "Presión": ["Pascales a Atmósferas", "Atmósferas a Pascales", "Barras a Libras por pulgada cuadrada", "Libras por pulgada cuadrada a Bares"],
    "Tamaño de Datos": ["Megabytes a Gigabytes", "Gigabytes a Terabytes", "Kilobytes a Megabytes", "Terabytes a Petabytes"]
}

# Seleccionar categoría
categoria_seleccionada = st.sidebar.selectbox("Selecciona una categoría", list(categorias.keys()))

# Seleccionar tipo de conversión dentro de la categoría seleccionada
conversion_seleccionada = st.sidebar.selectbox("Selecciona una conversión", categorias[categoria_seleccionada])

# Mostrar resultado de la conversión
st.write(f"Has seleccionado la conversión: {conversion_seleccionada}")
