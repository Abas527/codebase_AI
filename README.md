# AI Codebase Explainer

AI Codebase Explainer is a local Retrieval-Augmented Generation (RAG) system that enables developers to explore and understand software repositories using natural language.
It analyzes a repository, extracts function-level code chunks, embeds them into a vector database, and allows users to ask questions about the codebase through a conversational interface.

The system runs entirely locally using Ollama for the language model and supports interactive visualization of repository structure.

---

## Features

* Repository ingestion from GitHub URLs
* AST-based Python code parsing
* Function-level semantic code chunking
* Vector database for semantic retrieval
* Natural language querying of codebases
* File and line number references in answers
* Interactive chat interface
* Repository graph visualization
* Fully local execution with Ollama LLMs

---

## Architecture

The system follows a Retrieval-Augmented Generation architecture:

Repository
→ Clone & Ingestion
→ AST Parsing
→ Code Chunking
→ Embeddings Generation
→ Vector Database Storage
→ Semantic Retrieval
→ Local LLM Response Generation
→ Streamlit Interface

### Core Components

**Ingestion Pipeline**

* Clones repositories
* Extracts Python files
* Parses code using Python AST
* Generates function-level chunks

**Vector Store**

* Stores embeddings of code chunks
* Enables semantic retrieval

**RAG Engine**

* Retrieves relevant code context
* Combines context with user query
* Generates responses using a local LLM

**User Interface**

* Interactive chat interface
* Repository graph visualization
* GitHub repository loader

---

## Project Structure

```
codebase_AI
│
├── app
│   ├── ui.py
|   ├── app.py
│
├── ingestion
│   ├── repo_loader.py
│   ├── code_loader.py
│   ├── ast_chunker.py
│   ├── ingestion_pipeline.py
|   ├── create_vector_db.py
|   ├── create_repo_structure.py
|
│
├── rags
│   ├── rag_chain.py
│   ├── retriever.py
│   ├── model.py
│   └── prompt.py
│
├── utils
│   ├── code_graph.py
│   └── graph_visualizer.py
│
├── vector_db
├── uploads
└── README.md
```

---

## Requirements

* Python 3.9+
* Ollama
* Git

Python libraries:

```
streamlit
langchain
langchain-community
langchain-chroma
langchain-huggingface
chromadb
sentence-transformers
networkx
pyvis
```

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/Abas527/codebase_AI.git
cd codebase_AI
```

### 2. Create a virtual environment

```
python -m venv venv
source venv/bin/activate
```

Windows:

```
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## Install Local Language Model

Install Ollama from the official website and pull a supported model.

Example:

```
ollama pull phi3
```

The project is designed to work efficiently with lightweight local models.

---

## Running the Application

Start the Streamlit interface:

```
streamlit run app/ui.py
```

The application will be available at:

```
http://localhost:8501
```

---

## Usage

1. Open the web interface
2. Enter a GitHub repository URL
3. Click **Load Repository**
4. Wait for indexing to complete
5. Ask questions about the repository

Example queries:

```
Explain the architecture of this repository
Where is the pipeline function defined?
How does the ingestion pipeline work?
```

---

## Repository Graph Visualization

The system can generate a structural graph showing relationships between files and functions in the repository.

Steps:

1. Navigate to the **Repo Graph** tab
2. Click **Generate Repository Graph**
3. Explore the interactive visualization

---

## How It Works

### Code Parsing

The system uses Python AST parsing to extract:

* Functions
* Classes
* Code structure

Each function becomes an individual document chunk.

### Embedding Generation

Code chunks are embedded using a sentence-transformer model.

### Retrieval

Semantic search retrieves the most relevant code chunks based on the user query.

### Response Generation

The retrieved context is passed to a local language model through a RAG pipeline to generate an explanation.

---

## Example Output

When asking:

```
Explain the pipeline function
```

The system returns:

* A natural language explanation
* The relevant code snippet
* File location
* Line numbers

---

## Future Improvements

* Call graph generation
* Hybrid retrieval (BM25 + embeddings)
* Support for additional programming languages
* Repository-level summarization
* Docker deployment
* Code execution sandbox

---

## Contributing

Contributions are welcome.

Steps:

1. Fork the repository
2. Create a feature branch
3. Implement changes
4. Submit a pull request

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

* LangChain
* Chroma
* Ollama
* Streamlit
* Sentence Transformers
