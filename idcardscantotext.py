import streamlit as st
import cv2
import pytesseract
from PIL import Image
import numpy as np

# Set the title and description
st.title("ID Card Text Extraction")
st.write("Upload an image or use your camera to extract text from an ID card.")

# Create a file uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# Create a checkbox to use the camera
use_camera = st.checkbox("Use Camera")

# Initialize OpenCV VideoCapture if using the camera
if use_camera:
    cap = cv2.VideoCapture(0)

# Function to extract text from an image using Tesseract OCR
def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text

# Function to display the extracted text
def display_text(text):
    st.subheader("Extracted Text:")
    st.write(text)

if uploaded_file is not None:
    # Read the image from the uploaded file
    image = Image.open(uploaded_file)
    
    # Convert the PIL Image to a numpy array (OpenCV format)
    image_np = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Extract text from the image
    extracted_text = extract_text(image_np)

    # Display the extracted text
    display_text(extracted_text)

elif use_camera:
    # Read frames from the camera feed
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Extract text from the current frame
        extracted_text = extract_text(frame)

        # Display the extracted text
        display_text(extracted_text)

        # Display the camera feed with the detected text
        st.image(frame, channels="BGR")

# Release the camera if it was used
if use_camera:
    cap.release()

