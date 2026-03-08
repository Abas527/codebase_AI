import json
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import shutil
import os



def create_vector_db(chunks):
    if os.path.exists("vector_db"):
        print("Vector DB already exists")
        shutil.rmtree("vector_db")

    embedding_model=HuggingFaceEmbeddings(model_name="sentence-transformers/all-minilm-l6-v2")
    vector_db = Chroma.from_documents(chunks, embedding_model,persist_directory="vector_db")

    print("Vector DB created successfully")