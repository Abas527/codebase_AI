import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from rags.rag_chain import create_rag_chain
from ingestion.ingestion_pipeline import pipeline



def main():

    repo=input("Enter the repo url:")
    repo_path=pipeline(repo,destination_path="uploads")
    
    rag_chain=create_rag_chain(repo_path)

    
    while(1):
        inp=input("Ask Question about repo:")
        
        if inp=="q":
            break
        
        response=rag_chain.invoke(inp)
        print("Answer:\n")
        print(response)


if __name__ == "__main__":
    main()