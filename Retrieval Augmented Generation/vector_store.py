import os
import pickle
from config import get_document_embedder
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
import streamlit as st

def initialize_vector_store(_raw_documents):
    # Ensure the directory exists before accessing the file
    vector_store_dir = os.path.join(os.getcwd(), 'uploaded_docs')  # Absolute path using os.getcwd()
    if not os.path.exists(vector_store_dir):
        os.makedirs(vector_store_dir)  # Create the directory if it doesn't exist
        
    vector_store_path = os.path.join('./uploaded_docs', "vectorstore.pkl")
    if os.path.exists(vector_store_path):
        with open(vector_store_path, "rb") as f:
            vectorstore = pickle.load(f)
    else:
        if _raw_documents:
            text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
            documents = text_splitter.split_documents(_raw_documents)
            vectorstore = FAISS.from_documents(documents, get_document_embedder())
            with open(vector_store_path, "wb") as f:
                pickle.dump(vectorstore, f)
        else:
            vectorstore = None
    return vectorstore