from src.helper import load_pdf, text_split, download_hugging_face_embeddings
import pinecone
from dotenv import load_dotenv
import os
from langchain_pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore

"""
Loads environment variables from a .env file.

Example:
    load_dotenv()  # loads environment variables from a .env file
"""
load_dotenv()

"""
Gets the Pinecone API key from the environment variables.

Example:
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
"""
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

"""
Sets the Pinecone API key as an environment variable.

Example:
    os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
"""
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY


"""
Loads a PDF file and extracts its content.

Example:
    extracted_data = load_pdf('./data')
"""
extracted_data = load_pdf('./data')


"""
Splits the extracted PDF content into smaller chunks.

Example:
    text_chunks = text_split(extracted_data)
"""
text_chunks = text_split(extracted_data)


"""
Downloads Hugging Face embeddings.

Example:
    embeddings = download_hugging_face_embeddings()
"""
embeddings = download_hugging_face_embeddings()


"""
Creates a Pinecone client instance with the API key.

Example:
    pc = Pinecone(api_key=PINECONE_API_KEY)
"""
pc = Pinecone(api_key=PINECONE_API_KEY)


"""
Defines the name of the Pinecone index.

Example:
    index_name = "medical-chatbot"
"""
index_name = "medical-chatbot"


"""
Creates a Pinecone vector store from the text chunks and embeddings.

Example:
    docsearch = PineconeVectorStore.from_texts([i.page_content for i in text_chunks], embeddings, index_name=index_name)
"""
docsearch = PineconeVectorStore.from_texts([i.page_content for i in text_chunks], embeddings, index_name=index_name)