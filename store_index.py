from src.helper import load_pdf,text_split,download_hugging_face_embeddings
import pinecone
from dotenv import load_dotenv
import os
from langchain_pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
load_dotenv()
from pinecone import Pinecone


PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
os.environ['PINECONE_API_KEY'] =PINECONE_API_KEY


extracted_data=load_pdf('./data')

text_chunks=text_split(extracted_data)

embeddings=download_hugging_face_embeddings()



pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "medical-chatbot"

docsearch = PineconeVectorStore.from_texts([i.page_content for i in text_chunks],embeddings, index_name=index_name)


