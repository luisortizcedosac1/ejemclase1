import streamlit as st
import random

# Función para generar la ecuación de primer grado
def generar_ecuacion():
    a = random.randint(1, 10)
    b = random.randint(0, 10)
    x = random.randint(-10, 10)
    ecuacion_texto = f"{a}x + {b} = {a * x + b}"
    respuesta_correcta = x
    return ecuacion_texto, respuesta_correcta

st.title("Resolutor de ecuaciones de primer grado")
st.write("Ingresa tu respuesta (solo enteros) y verifica si es correcta.")

# Generar y almacenar la ecuación en la sesión
if 'ecuacion' not in st.session_state:
    ecuacion_texto, respuesta_correcta = generar_ecuacion()
    st.session_state['ecuacion'] = ecuacion_texto
    st.session_state['respuesta'] = respuesta_correcta

st.write(f"Ecuación: {st.session_state['ecuacion']}")

# Entrada del usuario
respuesta_usuario = st.number_input("Tu respuesta:", step=1)

# Botón para verificar
if st.button("Verificar respuesta"):
    if respuesta_usuario == st.session_state['respuesta']:
        st.success("¡Correcto! 🎉")
        # Mostrar globos (balloons)
        st.balloons()
        # Generar una nueva ecuación después de la celebración
        ecuacion_texto, respuesta_correcta = generar_ecuacion()
        st.session_state['ecuacion'] = ecuacion_texto
        st.session_state['respuesta'] = respuesta_correcta
    else:
        st.error("Respuesta incorrecta. Inténtalo de nuevo.")
