
from sentence_transformers import SentenceTransformer,util

def getEmbeddings(model_name,section,timestamps,similarity_method ):

    
    model = SentenceTransformer(model_name)
  
    model = SentenceTransformer(model_name)
    query_embedding = model.encode(section)
    corpus_embeddings = model.encode(timestamps)

    results = util.semantic_search(query_embedding, corpus_embeddings,
                                  score_function=similarity_method,top_k=20)
    results = sorted(results[0], key=lambda x: x['score'],reverse=True)
    
    final_result = []

    for d in results:
        ind = d['corpus_id']
        score = d['score']
        final_result.append((score, ind))
    return final_result

def createJson(results_list,section_text):
  import json
  texts = []
  scores = []
  for i in range(len(results_list)):
      text = results_list[i][0]
      score = results_list[i][2]
      texts.append(text)
      scores.append(score)
      dictionary = {'Judgement_Section': section_text}
      dictionary['Trancription'] = [{'Score': s, 'text': t} for s, t in zip(scores, texts)]
  with open('./jsonfiles/' + 'summary_semantic_search' +'.json', 'w') as fout:
    json.dump(dictionary , fout)
