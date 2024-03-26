# Project Description

This project is a Streamlit application called "StendhalGPT Gogh" that allows users to upload an image and detect regions of interest using the ELA (Error Level Analysis) method. The application uses OpenCV for image processing and Streamlit for the user interface.

[picture](https://github.com/zengdard/Streamlit_Analyse_Images/blob/main/donald_trump_marche_fake.jpg?raw=true)

## Features

- Allows users to upload an image in JPG, PNG, or JPEG format.
- Applies the ELA method to detect tampered areas in the image.
- Displays the uploaded image and the processed image with detected regions highlighted.

## Requirements

- OpenCV
- NumPy
- Streamlit
- PIL

## Usage

1. Run the application using Streamlit.
2. Upload an image using the file uploader.
3. The application will display the uploaded image and the processed image with detected regions highlighted.

## File Structure

- `main.py`: The main file containing the Streamlit application and the image processing code.

## Future Work

- Allow users to adjust the threshold value for ELA.
- Add support for other image processing techniques.
- Improve the user interface and error handling.

## Repository Name

A suitable name for this repository could be "Image-Tampering-Detection".
