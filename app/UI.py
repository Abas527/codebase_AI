import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
from rags.rag_chain import create_rag_chain
from ingestion.ingestion_pipeline import pipeline
from utils.code_graph import get_graph
from utils.graph_visualizer import visualize_graph
import streamlit.components.v1 as components
import time

st.set_page_config(
    page_title="AI Codebase Explainer",
    layout="wide"
)

st.title(" AI Codebase Explainer")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None


# Sidebar
with st.sidebar:

    st.header("Repository")

    repo_url = st.text_input("GitHub Repository URL")

    if st.button("Load Repository"):

        with st.spinner("Cloning and indexing repo..."):

            repo_path = pipeline(repo_url)
            st.session_state.rag_chain = create_rag_chain(repo_path)

        st.success("Repository ready!")


tab1, tab2 = st.tabs(["💬 Chat", "🧭 Repo Graph"])


with tab1:

    st.subheader("Chat with the Codebase")

    # Chat container (scrollable)
    chat_container = st.container()

    with chat_container:

        for message in st.session_state.messages:

            avatar = "👨‍💻" if message["role"] == "user" else "🤖"

            with st.chat_message(message["role"], avatar=avatar):
                st.markdown(message["content"])


    prompt = st.chat_input("Ask about the repository...")

    if prompt:

        if st.session_state.rag_chain is None:
            st.warning("Please load a repository first.")
            st.stop()

        # Save user message
        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        with st.chat_message("user", avatar="👨‍💻"):
            st.markdown(prompt)

        # Assistant response
        with st.chat_message("assistant", avatar="🤖"):

            response_placeholder = st.empty()
            full_response = ""

            response = st.session_state.rag_chain.invoke(prompt)

            # Fake streaming effect
            for word in response.split():
                full_response += word + " "
                time.sleep(0.02)
                response_placeholder.markdown(full_response)

        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )


with tab2:

    if repo_url:

        repo_name = repo_url.split("/")[-1]
        repo_path = f"uploads/{repo_name}"

        if st.button("Generate Repository Graph"):

            graph = get_graph(repo_path)

            html_file = visualize_graph(graph)

            HtmlFile = open(html_file, "r", encoding="utf-8")

            components.html(HtmlFile.read(), height=650)