# context/watchers/update_embeddings.py

import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# or from langchain.embeddings import HuggingFaceEmbeddings, etc.

def embed_files(files):
    # Initialize embeddings
    embeddings = OpenAIEmbeddings()  # or HuggingFaceEmbeddings()
    # Initialize vector store
    db = Chroma(collection_name="finance-project")
    
    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        # Create a doc with metadata
        doc = {"page_content": content, "metadata": {"file_path": file_path}}
        db.add_texts([doc["page_content"]], [doc["metadata"]])

    print(f"Embedded {len(files)} files into Chroma DB.")

if __name__ == "__main__":
    # Example usage: pass file paths via environment variable or CLI argument
    target_files = ["src/routes/user.js", "README.md"]
    embed_files(target_files)
