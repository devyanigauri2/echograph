import streamlit as st
import requests

# Streamlit App Title
st.title("Satvik")

# File Upload Section
uploaded_file = st.file_uploader("Upload an audio file", type=['wav', 'mp3', 'flac', 'ogg'])

# Backend API URL
BACKEND_URL = "http://127.0.0.1:5000/upload"

if uploaded_file is not None:
    st.write("File uploaded successfully:", uploaded_file.name)
    
    # Upload file to the backend
    if st.button("Upload"):
        files = {'file': (uploaded_file.name, uploaded_file.getvalue())}
        response = requests.post(BACKEND_URL, files=files)
        
        if response.status_code == 200:
            st.success(response.json().get('message', 'File uploaded successfully!'))
        else:
            st.error(response.json().get('error', 'Failed to upload file'))