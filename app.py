import os 
from dotenv import load_dotenv
from src.helper import load_pdf, text_split, download_hugging_face_embeddings

from langchain.vectorstores import Pinecone
import pinecone

from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from src.prompt import *
from langchain.llms import CTransformers

from flask import Flask, render_template, jsonify, request

from langchain_groq import ChatGroq

from langchain_pinecone import PineconeVectorStore




app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')


embeddings = download_hugging_face_embeddings()
    



index_name = "medical-chatbot"

# Loading the index
def load_index(index_name: str, embeddings: dict) -> PineconeVectorStore:
  
    # Loads an existing Pinecone index.

    # Args:
    #     index_name (str): Index name
    #     embeddings (dict): Embeddings dictionary

    # Returns:
    #     PineconeVectorStore: Loaded index
   
    return PineconeVectorStore.from_existing_index(index_name,embeddings)

docsearch = load_index(index_name, embeddings)


PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

def create_chain_type_kwargs(prompt: PromptTemplate) -> dict:
   
    # Creates chain type kwargs with prompt.

    # Args:
    #     prompt (PromptTemplate): Prompt template

    # Returns:
    #     dict: Chain type kwargs
   
    return {"prompt": prompt}

chain_type_kwargs = create_chain_type_kwargs(PROMPT)


def create_llm(groq_api_key: str, model: str) -> ChatGroq:
   
    # Creates a ChatGroq LLM.

    # Args:
    #     groq_api_key (str): Groq API key
    #     model (str): Model name

    # Returns:
    #     ChatGroq: LLM instance
    
    return ChatGroq(groq_api_key=groq_api_key, model=model)

groq_api_key = os.getenv("GROQ_API_KEY")
llm = create_llm(groq_api_key, "llama-3.1-8b-instant")


def create_retrieval_qa(llm: ChatGroq, retriever: PineconeVectorStore, chain_type_kwargs: dict) -> RetrievalQA:
  
    # Creates a RetrievalQA chain.

    # Args:
    #     llm (ChatGroq): LLM instance
    #     retriever (PineconeVectorStore): Retriever instance
    #     chain_type_kwargs (dict): Chain type kwargs

    # Returns:
    #     RetrievalQA: RetrievalQA chain instance
  
    return RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff", 
        retriever=retriever.as_retriever(search_kwargs={'k': 2}),
        return_source_documents=True, 
        chain_type_kwargs=chain_type_kwargs)

qa = create_retrieval_qa(llm, docsearch, chain_type_kwargs)


@app.route("/")
def index() -> str:
  
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat() -> str:
   
    msg = request.form["msg"]
    input = msg
    print(input)
    result = qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)