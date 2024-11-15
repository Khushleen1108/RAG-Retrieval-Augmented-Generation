import os
import streamlit as st

def handle_file_upload():
    with st.sidebar:
        st.subheader("Add to the Knowledge Base")
        with st.form("my-form", clear_on_submit=True):
            uploaded_files = st.file_uploader("Upload a file to the Knowledge Base:", accept_multiple_files=True)
            submitted = st.form_submit_button("Upload!")

        if uploaded_files and submitted:
            for uploaded_file in uploaded_files:
                with open(os.path.join('./uploaded_docs', uploaded_file.name), "wb") as f:
                    f.write(uploaded_file.read())
                st.success(f"File {uploaded_file.name} uploaded successfully!")