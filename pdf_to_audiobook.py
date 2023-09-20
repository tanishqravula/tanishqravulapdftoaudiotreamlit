import streamlit as st
import PyPDF2
import base64
from gtts import gTTS
import os

st.title("PDF to Audiobook Converter")

# Upload PDF file
pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if pdf_file is not None:
    # Read the PDF and extract text
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page_num in range(len(reader.pages)):
        text += reader.pages[page_num].extract_text()

    # Convert text to speech
    tts = gTTS(text)

    # Save the audio file
    audio_file_path = "output.mp3"
    tts.save(audio_file_path)

    # Display the audio player
    st.audio(audio_file_path, format="audio/mp3")

    # Provide download link for the audiobook
    st.markdown(f"**[Download Audiobook](data:audio/mp3;base64,{base64.b64encode(open(audio_file_path, 'rb').read()).decode()})**")

    # Clean up temporary audio file
    os.remove(audio_file_path)
