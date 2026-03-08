from langchain_ollama import ChatOllama


def load_llm():
    llm=ChatOllama(model="phi3:mini",temperature=0.1)
    return llm