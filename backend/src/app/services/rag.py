from langchain_groq import ChatGroq

from app.services.retrieval import retrieve_documents


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
)


def answer_question(question: str):

    documents = retrieve_documents(question)

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    prompt = f"""
You are a helpful assistant answering questions about a PDF.

Use ONLY the provided context to answer the question.

If the answer cannot be found in the context,
say that you don't know.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "sources": [
            {
                "page": doc.metadata.get("page"),
            }
            for doc in documents
        ],
    }