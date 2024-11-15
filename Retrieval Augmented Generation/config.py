import os
from dotenv import load_dotenv
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from functools import lru_cache

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
os.environ['GOOGLE_API_KEY'] = api_key

# Set up Embeddings
@lru_cache(maxsize=1)
def get_document_embedder():
    embedding_model_name = "sentence-transformers/all-MiniLM-l6-v2"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    return HuggingFaceEmbeddings(model_name=embedding_model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs)


# Initialize LLM
def initialize_llm():
    return ChatGoogleGenerativeAI(model='gemini-1.5-flash')