from langchain.document_loaders import DirectoryLoader,PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings



## Extract data from the PDF
def load_pdf(data_directory):
    loader=DirectoryLoader(data_directory,
                     glob="*.pdf",
                     loader_cls=PyPDFLoader,
                     show_progress=True)
    documents=loader.load()
    return documents


## Create Text Chunk
def text_split(extracted_data):
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20
    )
    text_chunks=text_splitter.split_documents(extracted_data)
    return text_chunks


## Download Embdedding Model
def download_hugging_face_embeddings():
    embedding=HuggingFaceEmbeddings(
       model_name="all-MiniLM-L6-v2",
       show_progress=True
    )
    return embedding