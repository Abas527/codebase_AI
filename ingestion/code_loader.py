import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from .ast_chunker import extract_function_and_class

IGNORE_DIRS=[
    ".git",
    "node_modules",
    "venv",
    "__pycache__",
    "dist",
    "build",
    "docs",
    "tests",
    "env"
]

def load_python_files(dir_path):
    python_files=[]

    for root,dirs,files in os.walk(dir_path):
        for dir in dirs:
            if dir in IGNORE_DIRS:
                dirs.remove(dir)

        for file in files:
            if file.endswith(".py") and file not in IGNORE_DIRS:
                python_files.append(os.path.join(root,file))

    return python_files

def read_files(python_files):
    documents=[]
    for file in python_files:
        try:
            with open(file,"r",encoding="utf-8") as f:
                code=f.read()
        except:
            raise Exception(f"Error reading file: {file}")
        
        documents.append({
            "content":code,
            "metadata":{
                "file_path":file,
                "language":"python",
                "name":os.path.basename(file)

            }
        })
    return documents

def chunking(documents):

    all_chunks=[]

    for doc in documents:
        code=doc["content"]
        metadata=doc["metadata"]
        path=metadata["file_path"]

        chunks=extract_function_and_class(code,path)
        all_chunks.extend(chunks)

    return all_chunks
