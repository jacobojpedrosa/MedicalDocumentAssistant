import requests
import json

class Ollama:
    
    
    def __init__(self, model_name, hf_token):
        self.model_name = model_name
        self.hf_token = hf_token
        self.ollama_url = "http://localhost:11434/api/generate"
    
    def make_question(self, question, context=""):
        print(f"OllamaURL: {self.ollama_url}")
        headers = { "Content-Type":"application/json"}
        
        prompt = f"""
            You are a professional and accurate medical assistant AI trained to answer user questions only using information from provided documents about diseases.
            You will receive:
            * A user question about a disease, symptom, treatment, prognosis, or related topic.
            * A context that contains relevant text from disease-related documents.
            Your instructions:
            1- Read the context and determine whether it includes enough information to answer the user’s question.
            2- If the context contains relevant details, use only that information to answer clearly and accurately.
            3- If the context is missing, unrelated, or insufficient, respond with:
                "I'm sorry, I don't have enough information from the documents to answer that question."
            Important rules:
            * Do not use outside or general medical knowledge. Your answers must be strictly based on the provided document excerpts.
            * Keep your tone professional, helpful, and easy to understand.
            * If necessary, suggest the user consult a medical professional for clarification or diagnosis.
            * Do not specify where is the information from.

            Example 1:
            Context: "Diabetes mellitus is characterized by high blood sugar levels and may require insulin therapy."
            Question: "What is diabetes?"
            Answer: "According to the documents, diabetes mellitus is characterized by high blood sugar levels and may require insulin therapy."

            Example 2:
            Context: (empty)
            Question: "What are the symptoms of meningitis?"
            Answer: "I'm sorry, I don't have enough information from the documents to answer that question."

            Context:
            {context}
            Question: 
            {question}
            Answer:"""
        
        print("- prompt:", prompt)
        
        data = {
            "model" : "medllama2:latest",
            "prompt" : prompt,
            "stream" : False
        }
        
        try:
            response = requests.post(self.ollama_url, headers=headers, data=json.dumps(data))
            response.raise_for_status()  # Lanza una excepción para códigos de error HTTP
            return response.json()["response"]
        except requests.exceptions.RequestException as e:
            print(f"Error al hacer la petición a la API de Ollama: {e}")
            return None
        except KeyError:
            print("Error: La respuesta de la API no contiene el campo 'response'.")
            return None