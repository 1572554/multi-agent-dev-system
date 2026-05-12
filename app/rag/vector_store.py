import chromadb

client = chromadb.Client()

collection = client.get_or_create_collection("dev-agent")

def save_context(doc_id: str, content: str):
    collection.add(
        documents=[content],
        ids=[doc_id]
    )

def search_context(query: str):
    return collection.query(
        query_texts=[query],
        n_results=3
    )