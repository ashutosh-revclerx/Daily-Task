# ==========================================
# Day 8: ChromaDB + Embeddings + Semantic Search
# ==========================================

import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

# -----------------------------
# 1. Load Embedding Model
# -----------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embedding(text: str):
    return model.encode(text).tolist()

# -----------------------------
# 2. Initialize ChromaDB (Local)
# -----------------------------
client = chromadb.Client(
    Settings(persist_directory="./chroma_data")
)

collection = client.get_or_create_collection(name="documents")

# -----------------------------
# 3. Store Documents
# -----------------------------
documents = [
    "PostgreSQL is a relational database",
    "MongoDB is a document-oriented NoSQL database",
    "Vector databases enable semantic search"
]

ids = ["doc1", "doc2", "doc3"]
embeddings = [generate_embedding(doc) for doc in documents]

collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=ids
)

print("✅ Documents stored in vector database")

# -----------------------------
# 4. Semantic Search
# -----------------------------
query = "Which database is NoSQL?"
query_embedding = generate_embedding(query)

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

print("\n🔍 Search Results:")
for doc, distance in zip(results["documents"][0], results["distances"][0]):
    if distance < 0.4:  # similarity threshold
        print(f"MATCH: {doc} | score: {distance}")
