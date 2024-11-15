# RAG-Retrieval_Augmented_Generation
## Overview:
RAG-Retrieval_Augmented_Generation is a content engine built to analyze and compare document content using state-of-the-art retrieval-augmented generation techniques. This app processes documents, stores them in a vectorized format, and allows users to query the information through an interactive chatbot. The application leverages Streamlit for the user interface and LangChain for integrating NLP components with FAISS for efficient vector storage.

## Features:
- **File Upload**: Upload multiple document types (TXT, PDF, DOCX) through a sidebar form.
- **Document Processing**: Parses and processes documents, storing them in a vector store for efficient retrieval.
- **Chat Interface**: Users can ask questions and get insights based on the context of uploaded documents.
- **Data Privacy**: Uses a locally running LLM, ensuring user data remains private.
- **Embeddings and Vector Search**: Utilizes FAISS and HuggingFace for creating and querying vectorized document embeddings.

## Architecture
The project structure ensures modularity and scalability:
- **Main App**: `main.py`
- **File Handling**: `handle_upload.py`
- **Document Loading**: `utils.py`
- **Vector Store Management**: `vector_store.py`
- **Chat Interface**: `chat_interface.py`
- **Configuration**: `config.py` for loading environment variables and initializing models.

## Project Structure:
```bash
RAG-Retrieval_Augmented_Generation/
│
├── main.py                 # Entry point for the app
├── config.py               # Configuration for models, environment variables, and embeddings
├── handle_upload.py        # Handles file upload logic
├── utils.py                # Utility functions for document loading
├── vector_store.py         # Vector store initialization and management
├── chat_interface.py       # Chat interface setup and user input handling
│
├── uploaded_docs/          # Directory for storing uploaded documents
│
├── .env                    # Environment variables (not included in version control)
├── .gitignore              # Lists files/directories to be ignored by Git
├── requirements.txt        # List of Python dependencies
└── README.md               # Project documentation
```

## Installation

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2. **Set Up the Environment**:
    Create a `.env` file with the following content:
    ```bash
    GOOGLE_API_KEY=your-google-api-key-here
    ```

3. **Install Dependencies**:
    Make sure you have Python 3.8+ installed and run:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the App**:
    ```bash
    streamlit run main.py

## Usage

1. **Upload Documents**:
   - Use the sidebar to upload files (TXT, PDF, DOCX). The uploaded documents will be processed and stored in the `uploaded_docs/` directory.
2. **Interact with the Chatbot**:
   - Enter your queries into the chat interface. The system will retrieve relevant information from the documents and provide an AI-generated response.

## Technologies Used
- **Streamlit**: For creating the web-based user interface.
- **LangChain**: For building chains involving LLMs.
- **HuggingFace Embeddings**: For generating document embeddings.
- **FAISS**: For efficient vector storage and retrieval.
- **PyPDF2** and **python-docx**: For parsing PDF and DOCX files.
- **Python-dotenv**: For managing environment variables.

## Documentation and User Guide
- **User Guide**:
  - Upload files using the sidebar form.
  - Enter a query in the chat interface to get responses based on the context of uploaded documents.

- **Documentation**:
  - All operations for document loading, vector store management, and query handling are well-commented in the codebase.
  - Ensure the `.env` file contains your `GOOGLE_API_KEY` for the app to function properly.

## License
[MIT License]

## Contact
For any questions or feedback, please contact Khushleen at k2aur8154@gmail.com.
