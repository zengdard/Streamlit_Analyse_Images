import cv2
import numpy as np
import streamlit as st

st.set_option('deprecation.showfileUploaderEncoding', False)

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

# Créer une interface utilisateur avec Streamlit
st.title("StendhalGPT Picture Detector")
uploaded_file = st.file_uploader("Upload your picture here [JPG, JPEG, PNG].", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
    show_filtered_image(image)
else:
    st.warning("Choose an other picture to check.")

