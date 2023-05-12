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


col5, col6 = st.columns(2)

if tabs == 'Accueil':

        st.title('ELA Filter Application')

        uploaded_file = st.file_uploader("Choose an image...", type="jpg")
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image.', use_column_width=True)
            st.write("")

            # Convertir l'image en un tableau numpy pour le traitement
            image = np.array(image)
            image_ela = image.copy()  # Copie de l'image pour l'appliquer sur le filtre ELA

            # Convertir l'image en niveaux de gris
            grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Appliquer le filtre ELA avec le filtre de différence absolue comme noyau
            ela = cv2.absdiff(grayscale, cv2.blur(grayscale, (5, 5)))

            # Seuiller l'image ELA pour obtenir une image binaire
            threshold_value = 10.5
            threshold = cv2.threshold(ela, threshold_value, 255, cv2.THRESH_BINARY)[1]

            # Effectuer une analyse de connectivité pour identifier les groupes de pixels connectés
            connectivity = 8
            output = cv2.connectedComponentsWithStats(threshold, connectivity, cv2.CV_32S)

            # Récupérer les informations sur les composantes connectées
            num_labels = output[0]
            labels = output[1]
            stats = output[2]

            # Parcourir les composantes connectées
            for label in range(1, num_labels):
                # Récupérer les coordonnées du rectangle englobant
                x, y, w, h = stats[label, cv2.CC_STAT_LEFT], stats[label, cv2.CC_STAT_TOP], stats[label, cv2.CC_STAT_WIDTH], stats[label, cv2.CC_STAT_HEIGHT]
                # Dessiner un carré autour du groupe de pixels

                if w*h > 60:
                    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.rectangle(image_ela, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Convertir les tableaux numpy en images PIL pour l'affichage
            image = Image.fromarray(image)
            image_ela = Image.fromarray(image_ela)

            # Afficher l'image avec les carrés dessinés
            st.image(image, caption='Image with detected regions.', use_column_width=True)
            st.image(image_ela, caption='ELA image with detected regions.', use_column_width=True)
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
