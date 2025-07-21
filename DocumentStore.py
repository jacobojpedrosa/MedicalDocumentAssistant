import chromadb
from sentence_transformers import SentenceTransformer

from langchain.text_splitter import RecursiveCharacterTextSplitter


class DocumentStore:
    def __init__(self, path="./data/chroma_db"):
        self.client = chromadb.PersistentClient(path=path)
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2") #all-MiniLM-L6-v2, medllama2, all-mpnet-base-v2
        self.collection = self.client.get_or_create_collection(name="medical_documents")

    def add_document(self, doc_id, document_content, metadata=None):
        print(f"Metadata: {metadata}")
        
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_text(document_content)
        print(f"Number of chunks: {len(chunks)}")
        for idx,chunk in enumerate(chunks):
            chunk_id = f"{doc_id}_{idx}"
            self.collection.add(
                documents=[chunk],
                metadatas=[metadata],
                ids=[chunk_id]
            )

    def query_documents(self, query_text, n_results=5):
        query_embedding = self.embedding_model.encode(query_text).tolist()
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
        return results

