from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings


## Extract data from the PDF
def load_pdf(data_directory):
    """
    Load PDF files from a directory and extract their content.

    Args:
        data_directory (str): The directory containing the PDF files.

    Returns:
        list: A list of Document objects containing the extracted text.

    Example:
        >>> documents = load_pdf("/path/to/pdfs")
        >>> print(len(documents))  # prints the number of PDF files loaded
    """
    loader = DirectoryLoader(data_directory,
                             glob="*.pdf",
                             loader_cls=PyPDFLoader,
                             show_progress=True)
    documents = loader.load()
    return documents


## Create Text Chunk
def text_split(extracted_data):
    """
    Split the extracted text into chunks of a specified size.

    Args:
        extracted_data (list): A list of Document objects containing the extracted text.

    Returns:
        list: A list of text chunks.

    Example:
        >>> documents = load_pdf("/path/to/pdfs")
        >>> text_chunks = text_split(documents)
        >>> print(len(text_chunks))  # prints the number of text chunks
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20
    )
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks


## Download Embedding Model
def download_hugging_face_embeddings():
    """
    Download a Hugging Face embedding model.

    Returns:
        HuggingFaceEmbeddings: An instance of the Hugging Face embedding model.

    Example:
        >>> embedding = download_hugging_face_embeddings()
        >>> print(embedding.model_name)  # prints the name of the downloaded model
    """
    embedding = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
        show_progress=True
    )
    return embedding