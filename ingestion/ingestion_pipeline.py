import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from .repo_loader import repo_loader
from .code_loader import read_files, load_python_files, chunking
from .create_vector_db import create_vector_db

def pipeline(repo_url,destination_path="uploads"):

    print("Repo loading...")
    repo_path=repo_loader(repo_url,destination_path)

    print("Code loading...")
    # code loading
    python_files=load_python_files(destination_path)

    # code reading
    print("Code reading...")
    raw_docs=read_files(python_files)
    print("Code reading done...")

    # chunking
    print("Documents chunking...")
    chunks=chunking(raw_docs)
    print("Documents chunking done...")

    # vector db creation
    print("Vector DB creation...")
    create_vector_db(chunks)
    print("Vector DB creation done...")

    return repo_path
