import gensim
from gensim.similarities import Similarity
from gensim.test.utils import common_corpus, common_dictionary, get_tmpfile
from gensim.similarities import MatrixSimilarity

def tf_idf_similarity(section,timestamps):
  """ 
    Method takes a judgement section and relevant timestamps and returns similarity scores and indices:
    :param section: judgement section (str)
    :param timestamps: list of timestamps (list)
    returns results as tuples of similarity score and timestamp index
    """

  timestamps.insert(0,section)
  clean_trans_summary = []
  for text in timestamps:
    clean_trans_summary.append(gensim.utils.simple_preprocess(text))
  dictionary = gensim.corpora.Dictionary(clean_trans_summary)
  corpus = [dictionary.doc2bow(text) for text in clean_trans_summary]
  tf_idf=gensim.models.TfidfModel(corpus)
  # workign with bigger corpus use the below two lines, careful as it repeats results with several runs
  # index_tmpfile = get_tmpfile("./index")
  #similarity_object = Similarity(index_tmpfile, tf_idf[corpus], num_features=len(dictionary))
  #for smaller corpus calculate cosine similarity from memory
  similarity_object = MatrixSimilarity(tf_idf[corpus], num_features=len(dictionary))
  query= gensim.utils.simple_preprocess(section)
  query_bow=dictionary.doc2bow(query)
  query_tfidf=tf_idf[query_bow]
  similarity_scores =list(similarity_object[query_tfidf])
  similarity_scores = similarity_scores[1:]
  sorted_scores = sorted(similarity_scores, reverse=True)
  #get index of the raw text according to similarity scores
  ind= []
  for i in range(len(sorted_scores)):
    ind.append(similarity_scores.index(sorted_scores[i]))

  return list(zip(sorted_scores,ind))



