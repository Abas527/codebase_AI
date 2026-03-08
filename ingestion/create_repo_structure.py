import os

def store_repo_structure(repo_path):
    structure=[]

    for root,dirs,files in os.walk(repo_path):
        level=root.replace(repo_path,'').count(os.sep)
        indent=level*'\t'
        structure.append(f'{indent}{os.path.basename(root)}')
        subindent=(level+1)*'\t'
        for file in files:
            if file.endswith('.py'):
                structure.append(f'{subindent}{file}')


    return '\n'.join(structure)