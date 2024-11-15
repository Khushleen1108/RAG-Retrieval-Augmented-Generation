import streamlit as st
from config import initialize_llm
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = initialize_llm()

def setup_chat_interface():
    st.subheader("Chat with your AI Assistant!")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handle_user_input(vectorstore):
    prompt_template = ChatPromptTemplate.from_messages([("system", "You are a helpful AI assistant"), ("user", "{input}")])
    chain = prompt_template | llm | StrOutputParser()

    user_input = st.chat_input("Ask your question:")
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.markdown(user_input)

        if vectorstore is not None:
            retriever = vectorstore.as_retriever()
            context = "\n\n".join(doc.page_content for doc in retriever.get_relevant_documents(user_input))
            augmented_user_input = f'Context: {context}\n\nQuestion: {user_input}'

            response = chain.invoke({"input": augmented_user_input})

            st.session_state.messages.append({"role": "assistant", "content": response})

            with st.chat_message("assistant"):
                st.markdown(response)