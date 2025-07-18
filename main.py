import os
import streamlit as st


def main():
    st.title("Document Search App")


    uploaded_files = st.file_uploader("Upload documents", type=["txt", "pdf"], accept_multiple_files=True)
    if uploaded_files:
        documents = []
        for file in uploaded_files:
            print(f"{file.name} - {file.type}")
        #     if file.type == "text/plain":
        #         documents.append(file.getvalue().decode("utf-8"))

    query = st.text_input("Search query:")
    if query:
        print(f"query: {query}")
    

if __name__ == "__main__":
    main()






