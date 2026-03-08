import os
import subprocess
def repo_loader(repo_url,destination_path="uploads"):
    
    repo_name=repo_url.split("/")[-1].replace(".git","")
    repo_path=os.path.join(destination_path,repo_name)
    

    if os.path.exists(repo_path):
        return repo_path
    else:
        subprocess.run(["git", "clone", repo_url, repo_path],check=True)
        print("Repo cloned successfully")
        return repo_path


if __name__=="__main__":
    repo_url=input("Enter the repo url:")
    destination_path=input("Enter the destination path:")
    repo_loader(repo_url,destination_path)