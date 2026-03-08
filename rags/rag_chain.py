from langchain_core.prompts import PromptTemplate,ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable,RunnablePassthrough,RunnableParallel
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from .model import load_llm
from .retriever import retriever
from .prompt import get_prompt
from ingestion.create_repo_structure import store_repo_structure


def format_docs(docs):
    formatted=[]
    for doc in docs:

        source=doc.metadata.get("source")
        name=doc.metadata.get("name")
        start=doc.metadata.get("start_line")
        end=doc.metadata.get("end_line")

        formatted.append(
            f""" 
            FILE: {source} 
FUNCTION: {name}
LINE: {start}

CODE:
{doc.page_content}
            """
        )
    return "\n\n".join(formatted)

def create_rag_chain(repo_path):
    llm=load_llm()
    retr=retriever()

    repo_structure=store_repo_structure(repo_path)

    prompt=get_prompt()
    
    rag_chain=(
        {
            "context": retr|format_docs,
            "question": RunnablePassthrough(),
            "repo_structure":lambda x: repo_structure
        }|prompt|llm|StrOutputParser()
    )
    return rag_chain