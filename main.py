import os
import pdfplumber
import streamlit as st
from DocumentStore import DocumentStore as DocumentStore
from Agents.OllamaAgent import Ollama as Ollama
from dotenv import load_dotenv




def main():
    load_dotenv()

    base_model = os.getenv("BASE_MODEL")
    hf_token = os.getenv("HF_TOKEN")
    
    store = DocumentStore()
    ollama = Ollama(base_model, hf_token)



    # Initialize session state
    if "documents" not in st.session_state:
        st.session_state.documents = []

    st.title("MEDICAL DOCUMENT ASSISTANT")

    uploaded_files = st.file_uploader("Upload documents", type=["txt", "pdf"], accept_multiple_files=True)
    if uploaded_files and not st.session_state.documents:
        documents = []
        files_processed = 0
        total_files = len(uploaded_files)
        percent_complete = 0
        
        progress_bar = st.progress(0, text=f"Processing {total_files} files. Please wait...")

        for file in uploaded_files:
            if file.type == "text/plain":
                print(f"Adding text document: {file.name} - {file.type}")
                store.add_document(file.name, file.getvalue().decode("utf-8"), {"type": "text", "doc_name":file.name})
                documents.append(file.name)
                print("File stored")
                files_processed += 1

                
            if file.type == "application/pdf":
                print(f"Adding text document: {file.name} - {file.type}")
                # documents.append(file.name)

                # Extract text from PDF
                pdf_text = ""
                with pdfplumber.open(file) as pdf:
                    for page in pdf.pages:
                        text = page.extract_text()
                        if text:  # Ensure the page is not empty
                            pdf_text += text + "\n"  # Adding a empyty line between pages
                
                store.add_document(file.name, pdf_text, {"type": "pdf", "doc_name":file.name})
                documents.append(file.name)
                print("File stored")
                files_processed += 1

            
            percent_complete = files_processed / total_files
            print(f"Percent complete: {percent_complete}")
            progress_bar.progress(percent_complete, text=f"Processed {files_processed}/{total_files} files. Please wait...")
        
        print(f"All files stored {len(uploaded_files)}")
        progress_bar.empty().empty()
        st.session_state.documents = documents



    query = st.text_input("Search query:")
    if query:
        print(f"query: {query}")
        results = store.query_documents(query)
        # print(f"results: {results}")
        for i in range(len(results['documents'][0])):
            print(f"Results: {i}")
            print(f"File: {results['metadatas'][0][i]['doc_name']}")
            print(f"Chunk id: {results['ids'][0][i]}")
            print(f"Distance: {results['distances'][0][i]}")
        

        print(f"File extract: {results['documents'][0][0]}")        
        # st.write(f"File extract: {results['documents'][0][0]}")

        response = ollama.make_question(query, results['documents'][0][0])
        print(f"Response: {response}")
        st.write(f"Document: {results['metadatas'][0][0]['doc_name']}")
        st.write(f"Answer: {response}")
    

if __name__ == "__main__":
    main()






