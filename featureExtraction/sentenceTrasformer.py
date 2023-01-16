

from sentence_transformers import SentenceTransformer,util
model = SentenceTransformer('all-MiniLM-L6-v2')

def getEmbeddings(model_name,section,timestamps):
  
    model = SentenceTransformer(model_name)
    query_embedding = model.encode(section)
    corpus_embeddings = model.encode(timestamps)

    results = util.semantic_search(query_embedding, corpus_embeddings)
    results = sorted(results[0], key=lambda x: x['score'],reverse=True)
    
    final_result = []

    for d in results:
        ind = d['corpus_id']
        score = d['score']
        final_result.append((timestamps[ind], section,score))
    return final_result