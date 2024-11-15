from handle_upload import handle_file_upload
from utils import load_documents_from_directory
from vector_store import initialize_vector_store
from chat_interface import setup_chat_interface, handle_user_input

# Main function to drive the app
def main():
    handle_file_upload()
    raw_documents = load_documents_from_directory()
    vectorstore = initialize_vector_store(raw_documents)
    setup_chat_interface()
    handle_user_input(vectorstore)

if __name__ == "__main__":
    main()