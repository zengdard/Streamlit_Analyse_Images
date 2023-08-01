import cv2
import numpy as np
import streamlit as st
st.set_option('deprecation.showfileUploaderEncoding', False)
from PIL import Image 
from st_on_hover_tabs import on_hover_tabs
st.title("StendhalGPT Gogh")



col5, col6 = st.columns(2)


uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png","jpeg"])
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

                if w*h > 280:
                    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.rectangle(grayscale, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Convertir les tableaux numpy en images PIL pour l'affichage
        image = Image.fromarray(image)
        image_ela = Image.fromarray(grayscale)

        # Afficher l'image avec les carrés dessinés
        st.image(image, caption='Image with detected regions.', use_column_width=True)
        st.image(ela, caption='ELA image with detected regions.', use_column_width=True)
