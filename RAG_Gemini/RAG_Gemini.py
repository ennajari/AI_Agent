import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI

# Clé API Gemini
GEMINI_API_KEY = "AIzaSyAczCyyNGdK7xsBSu2itvilLGMtn6d0QiY"

def main():
    st.set_page_config(layout="wide")
    st.subheader("RAG Chatbot (Gemini)", divider="rainbow")

    with st.sidebar:
        st.sidebar.title("Data Loader")
        st.image("rag.png", width=500)
        pdf_docs = st.file_uploader("Upload Your PDFs", accept_multiple_files=True)

        if st.button("Submit"):
            with st.spinner("Loading..."):
                pdf_content = ""
                for pdf in pdf_docs:
                    reader = PdfReader(pdf)
                    for page in reader.pages:
                        text = page.extract_text()
                        if text:
                            pdf_content += text

                # Chunking
                text_splitter = CharacterTextSplitter(
                    separator="\n",
                    chunk_size=1000,
                    chunk_overlap=200,
                    length_function=len,
                )
                chunks = text_splitter.split_text(pdf_content)
                st.write(chunks)

                # Embedding & Vector Store (Gemini)
                embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GEMINI_API_KEY)
                vector_store = FAISS.from_texts(chunks, embedding=embeddings)

                # LLM (Gemini)
                llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GEMINI_API_KEY)

                # Prompt template
                prompt = ChatPromptTemplate.from_template(
                    """
                    Answer the following question based only on the provided context:
                    <context>
                    {context}
                    </context>
                    Question: {input}
                    """
                )

                # Retrieval chain
                document_chain = create_stuff_documents_chain(llm, prompt)
                retriever = vector_store.as_retriever()
                retrieval_chain = create_retrieval_chain(retriever, document_chain)

                st.session_state.retrieval_chain = retrieval_chain

    st.subheader("Chatbot zone")
    user_question = st.text_input("Ask your question :")
    if user_question:
        response = st.session_state.retrieval_chain.invoke({"input": user_question})
        st.markdown(response["answer"], unsafe_allow_html=True)


if __name__ == "__main__":
    main()
