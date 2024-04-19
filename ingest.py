import os
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.document_loaders import (
    DirectoryLoader,
    # UnstructuredFileLoader,
    UnstructuredPDFLoader,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Qdrant

embeddings = SentenceTransformerEmbeddings(
    model_name="neuml/pubmedbert-base-embeddings"
)

print("Initializing Loader...")

loader = DirectoryLoader(
    "data/",
    glob="**/*.pdf",
    show_progress=True,
    loader_cls=UnstructuredPDFLoader,
)

print("Loading files...")
documents = loader.load()

print("Initializing splitter...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=70)

print("Splitting documents...")
texts = text_splitter.split_documents(documents)

# print(texts[1])

url = "http://localhost:6333"

print("Creating Qdrant db")
qdrant = Qdrant.from_documents(
    texts, embeddings, url=url, prefer_grpc=False, collection_name="vector_db2"
)

print("Qdrant DB is created...")
