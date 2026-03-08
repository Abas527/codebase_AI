import ast
import os
import networkx as nx


def get_graph(repo_path):
    graph = nx.DiGraph()

    for root, _, files in os.walk(repo_path):

        for file in files:

            if file.endswith(".py"):

                file_path = os.path.join(root, file)

                graph.add_node(file, type="file")

                with open(file_path, "r", encoding="utf-8") as f:
                    code = f.read()

                try:
                    tree = ast.parse(code)

                    for node in ast.walk(tree):

                        if isinstance(node, ast.FunctionDef):

                            func_name = node.name

                            graph.add_node(func_name, type="function")

                            graph.add_edge(file, func_name)

                except:
                    pass

    return graph