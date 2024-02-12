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
    "Peso/Masa": {
        "Libras a Kilogramos": lambda lbs: lbs * 0.453592,
        "Kilogramos a Libras": lambda kg: kg / 0.453592,
        "Onzas a Gramos": lambda oz: oz * 28.3495,
        "Gramos a Onzas": lambda g: g / 28.3495
    },
    "Volumen": {
        "Galones a Litros": lambda gal: gal * 3.78541,
        "Litros a Galones": lambda l: l / 3.78541,
        "Pulgadas cúbicas a Centímetros cúbicos": lambda in3: in3 * 16.3871,
        "Centímetros cúbicos a Pulgadas cúbicas": lambda cm3: cm3 / 16.3871
    },
    "Tiempo": {
        "Horas a Minutos": lambda horas: horas * 60,
        "Minutos a Segundos": lambda mins: mins * 60,
        "Días a Horas": lambda dias: dias * 24,
        "Semanas a Días": lambda semanas: semanas * 7
    },
    "Velocidad": {
        "Millas por hora a Kilómetros por hora": lambda mph: mph * 1.60934,
        "Kilómetros por hora a Metros por segundo": lambda kmh: kmh / 3.6,
        "Nudos a Millas por hora": lambda knots: knots * 1.15078,
        "Metros por segundo a Pies por segundo": lambda ms: ms * 3.28084
    },
    "Área": {
        "Metros cuadrados a Pies cuadrados": lambda m2: m2 * 10.7639,
        "Pies cuadrados a Metros cuadrados": lambda ft2: ft2 / 10.7639,
        "Kilómetros cuadrados a Millas cuadradas": lambda km2: km2 * 0.386102,
        "Millas cuadradas a Kilómetros cuadrados": lambda mi2: mi2 / 0.386102
    },
    "Energía": {
        "Julios a Calorías": lambda j: j / 4.184,
        "Calorías a Kilojulios": lambda cal: cal * 4.184,
        "Kilovatios-hora a Megajulios": lambda kwh: kwh * 3.6,
        "Megajulios a Kilovatios-hora": lambda mj: mj / 3.6
    },
    "Presión": {
        "Pascales a Atmósferas": lambda pa: pa / 101325,
        "Atmósferas a Pascales": lambda atm: atm * 101325,
        "Barras a Libras por pulgada cuadrada": lambda bar: bar * 14.5038,
        "Libras por pulgada cuadrada a Bares": lambda psi: psi / 14.5038
    },
    "Tamaño de Datos": {
        "Megabytes a Gigabytes": lambda mb: mb / 1024,
        "Gigabytes a Terabytes": lambda gb: gb / 1024,
        "Kilobytes a Megabytes": lambda kb: kb / 1024,
        "Terabytes a Petabytes": lambda tb: tb / 1024
    }
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
