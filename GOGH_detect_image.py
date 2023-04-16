import cv2
import numpy as np
import streamlit as st
st.set_option('deprecation.showfileUploaderEncoding', False)
from PIL import Image 
from st_on_hover_tabs import on_hover_tabs
st.title("StendhalGPT Gogh")

with st.sidebar:
        tabs = on_hover_tabs(tabName=['Accueil','Example'], 
                            iconName=['dashboard','home'],
                            styles = {'navtab': {'background-color':'#FFFFFF',
                                                'color': '#000000',
                                                'font-size': '18px',
                                                'transition': '.3s',
                                                'white-space': 'nowrap',
                                                'text-transform': 'uppercase'},
                                    'tabOptionsStyle': {':hover :hover': {'color': 'red',
                                                                    'cursor': 'pointer'}},
                                    'iconStyle':{'position':'fixed',
                                                    'left':'7.5px',
                                                    'text-align': 'left'},
                                    'tabStyle' : {'list-style-type': 'none',
                                                    'margin-bottom': '30px',
                                                    'padding-left': '30px'}},
                            key="1")
# Créer une fonction pour appliquer le filtre de Sobel
def sobel_filter(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convertir l'image en niveau de gris
    grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3) # appliquer le filtre de Sobel sur l'axe X
    grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3) # appliquer le filtre de Sobel sur l'axe Y
    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)
    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    return grad

# Créer une fonction pour afficher l'image et appliquer le filtre
def show_filtered_image(image):
    st.image(image, caption='Image originale', use_column_width=True)
    filtered_image = sobel_filter(image)
    st.image(filtered_image, use_column_width=True)

col5, col6 = st.columns(2)

if tabs == 'Accueil':
    uploaded_file = st.file_uploader("Choisissez une image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
        show_filtered_image(image)
    else:
        st.warning("Veuillez choisir une image à filtrer.")
elif tabs == 'Example' :
    with col5:
        st.markdown('## Problèmes typiques d\'une génération :')
        st.markdown("""
    <ul>
        <li>Éléments notables distordus ou faux (Drapeaux, logos, éléments distinctifs, etc)</li>
        <li>Netteté ou incohérence d'éléments précis (Visages, mains, insignes) </li>
        <li>Ombres mals représentées</li>
    </ul>
    """, unsafe_allow_html=True)
        

        image = Image.open('donald_trump_marche_fake.png')
        st.image(image, caption='Image Générée')
        image = Image.open('pape_fake_2.jpg')
        st.image(image, caption='Image Générée')
    with col6:
        
        st.markdown('## Éléments à prendre en compte :')
        st.markdown("""
    <ul>
        <li>Qualité et netteté générale de la photo</li>
    </ul>
    """, unsafe_allow_html=True)
        image = Image.open('pape_true.jpg')
        st.image(image, caption='Image Non Générée')

        image = Image.open('fake_generate.jpg')
        st.image(image, caption='Image Non Générée')
        image = Image.open('fake_generate_2.jpg')
        st.image(image, caption='Image Non Générée')
