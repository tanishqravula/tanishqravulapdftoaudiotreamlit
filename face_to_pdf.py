import streamlit as st
import cv2
import base64
from fpdf import FPDF
import numpy as np

st.title("Face to PDF Converter")

# Upload an image with a face
uploaded_image = st.file_uploader("Upload an image with a face", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Load the uploaded image
    image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), cv2.IMREAD_COLOR)

    # Display the image
    st.image(image, caption="Uploaded Image with Face", use_column_width=True)

    # Collect personal details through a web form
    st.subheader("Enter Personal Details")
    name = st.text_input("Name")
    age = st.text_input("Age")
    address = st.text_input("Address")

    if st.button("Generate PDF"):
        # Create a PDF with personal details
        pdf_path = "user_details.pdf"
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add personal details to the PDF
        pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
        pdf.cell(200, 10, txt=f"Age: {age}", ln=True)
        pdf.cell(200, 10, txt=f"Address: {address}", ln=True)

        # Save the PDF file
        pdf.output(pdf_path)

        st.success("PDF with personal details saved.")
        st.markdown(f"[Download PDF](data:application/pdf;base64,{base64.b64encode(open(pdf_path, 'rb').read()).decode()})")
