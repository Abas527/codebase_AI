from langchain_core.prompts import PromptTemplate,ChatPromptTemplate
from langchain_core.runnables import Runnable,RunnablePassthrough,RunnableParallel

prompt=ChatPromptTemplate.from_template(
"""
You are an expert Python engineer.

Use the code context to answer the question.

Always mention:
- function name
- file name
- line number

REPOSITORY STRUCTURE:
{repo_structure}

CODE CONTEXT:
{context}

QUESTION:
{question}

Provide a clear explanation for a developer.
"""
)

def get_prompt():
    return prompt