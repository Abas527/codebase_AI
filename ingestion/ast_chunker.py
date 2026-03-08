import ast
from langchain_core.documents import Document

def extract_function_and_class(code,file_path):

    try:
        tree = ast.parse(code)
    except (SyntaxError, TabError) as exc:
        try:
            normalized = code.replace("\t", "    ")
            tree = ast.parse(normalized)
        except Exception:
            print(f"[ingestion] skipping {file_path}: parse error {exc}")
            return []

    chunks=[]

    for node in ast.walk(tree):

        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            start=node.lineno-1
            end=node.end_lineno
            chunk=code[start:end+1]

            lines=code.splitlines()[start:end+1]
            snippet="\n".join(lines)

            chunks.append(Document(

                page_content=snippet,
                metadata={"source":file_path,
                          "type":type(node).__name__,
                          "name":node.name,
                          "start_line":start,
                          "end_line":end
                          }
            ))

    return chunks