# MedicalDocumentAssistant

This project is a Streamlit-based application that allows users to upload medical documents (PDF or TXT), search within them using a query, and receive contextualized answers using a local language model (via the Ollama API).

It combines:

* PDF and text processing (pdfplumber)

* Document storage and retrieval (DocumentStore)

* Contextual Q&A with a local LLM (Ollama)

* Streamlit interface for ease of use

## Features
* Upload and extract text from multiple PDF or TXT medical documents.

* Query documents using natural language.

* Get accurate answers based only on document context.

* Interactive UI with progress bar and session memory.


## Example Query
Query: What is diabetes?
Answer: According to the documents, diabetes mellitus is characterized by high blood sugar levels and may require insulin therapy.

## Notes
The application does not use external medical knowledge—only what's in the documents.

Ideal for confidential document search or medical assistants running locally.




# Installation
1. Clone the repository

```bash
git clone https://github.com/jacobojpedrosa/MedicalDocumentAssistant.git
cd MedicalDocumentAssistant
````

2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```


3. Install requirements

```bash
pip install -r requirements.txt
```


4. Set Environment Variables
Create a .env file in the project root with:

```
OLLAMA_BASE_MODEL=your_model_name_here
HF_TOKEN=your_huggingface_token_if_needed
```

Or you can rename the env_sample file and set the Variables values.

5. Run

```bash
streamlit run main.py
```


# Usage

* Upload your PDF or TXT medical documents.

* Enter a search query (e.g., "What are the symptoms of diabetes?").

* The app finds the most relevant document chunks and sends them to the model.

* You get an answer based only on the document content.

