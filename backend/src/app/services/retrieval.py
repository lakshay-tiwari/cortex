from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def get_retriever():

    vector_store = QdrantVectorStore.from_existing_collection(
        embedding=embeddings,
        url="http://localhost:6333",
        collection_name="cortex",
    )

    return vector_store.as_retriever(
        search_kwargs={"k": 4}
    )


def retrieve_documents(question: str):

    retriever = get_retriever()

    return retriever.invoke(question)