from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


def retriever():

    embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-minilm-l6-v2")
    

    vector_db=Chroma(persist_directory="vector_db",embedding_function=embedding)

    retriev=vector_db.as_retriever(
        search_kwargs={
            "k": 6,
            "fetch_k": 20
        },search_type="mmr"
    )

    return retriev
