from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore


# 1. Load PDF
loader = PyPDFLoader("example.pdf")
documents = loader.load()

print(f"Loaded {len(documents)} pages")


# 2. Split PDF into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")


# 3. Create embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# 4. Store chunks + embeddings in Qdrant
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="pdf_documents",
    path="./qdrant_data"
)

print("PDF chunks stored in Qdrant!")