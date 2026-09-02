from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer
from preprocess import prepare_data

def encoder():
    encoder = SentenceTransformer('all-MiniLM-L6-v2')
    return encoder


def generate_embbedings(records, encoder):
    print('Phase 2: generating embeddings')

    documents = []
    metadata = []

    # separate text and metadata
    for record in records:
        documents.append(record['headline'])
        metadata.append({'sentiment': record['sentiment']})

    print(f'vectorizing {len(documents)}...')

    embeddings = encoder.encode(documents, show_progress_bar=True)

    print('embedding completed!!!')

    return documents, metadata, embeddings



