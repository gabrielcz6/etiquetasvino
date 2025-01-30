import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from utils.utils import WineLabelGenerator

# Función para crear etiqueta
def crear_etiqueta():
    st.header("Crear Etiqueta")
    
    # Crear el generador de etiquetas
    generador = WineLabelGenerator()
    
    # Caja de texto para el input del usuario
    user_input = st.text_area("Introduce el prompt para la etiqueta", "")
    
    # Botón para generar las imágenes
    if st.button("Generar"):
        if user_input:
            # Mostrar el mensaje de esperando
            with st.spinner("Esperando... Generando las imágenes..."):
                # Generar las 3 imágenes basadas en el input del usuario
                imagenes = generador.generate_label_and_images(user_input)
            
            # Mostrar mensaje de generación completada
            st.success("¡Generado!")
            
            # Crear 3 columnas para mostrar las imágenes
            col1, col2, col3 = st.columns(3)
            
            # Mostrar las imágenes generadas en las columnas
            with col1:
                st.image(imagenes[0])
            with col2:
                st.image(imagenes[1])
            with col3:
                st.image(imagenes[2])
        else:
            st.warning("Por favor, ingresa un prompt antes de generar las imágenes.")

# Función principal
def app():
    # Título de la aplicación
    st.title("Aplicación generativa de etiquetas :cupid:")
    
    with st.sidebar:
        # Barra lateral (Sidebar)
        # Imagen en la barra lateral
        st.sidebar.image("personalw.png", width=290)

        # Menú lateral con opciones (usando streamlit-option-menu)
        menu = option_menu(
            menu_title='Menu',  # Título del menú
            options=['Crear etiqueta'],  # Opciones del menú
            icons=['wine'],  # Iconos de las opciones
            menu_icon="list",  # Ícono del menú lateral
            default_index=0,  # Índice por defecto
            styles={  # Estilos personalizados
                "container": {"padding": "5!important", "background-color": "#4B2E83"},  # Fondo púrpura vino
                "icon": {"color": "#9B1C31", "font-size": "23px"},  # Icono color rojo vino
                "nav-link": {
                    "color": "#C34A72",  # Texto en un tono vino suave
                    "font-size": "20px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#9B1C31"  # Color al pasar el cursor (rojo vino)
                },
                "nav-link-selected": {"background-color": "#5E2B3C"},  # Fondo de opción seleccionada (vino oscuro)
            }
        )
        # Lógica según la opción seleccionada
    if menu == "Crear etiqueta":
        crear_etiqueta()

# Ejecutar la aplicación
if __name__ == "__main__":
    app()
