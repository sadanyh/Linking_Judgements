import math
import json
import numpy as np
from numpy import dot
from numpy.linalg import norm



def calculate_cosine_similarity(a, b):

    """Method to get the similarity scores along with the timestamp index
    param a: timestamp embeddings (list )
    param b: section embedding ( numpy_array)
    """  
    sims = []
    ind= []    
    cos_sim = np.dot(a,b) / (norm(a, axis=1)*norm(b))
    sims.append(cos_sim)
    sorted_scores = sorted(sims, reverse=True)
    for i in range(len(sorted_scores)):
      ind.append(sims.index(sorted_scores[i]))
    return list(zip(sorted_scores,ind))
     
  
  #get index of the raw text according to similarity scores
  

# function to create a json file with the results of the cosine similarity measure

def get_results(cosine,k,timestamps_ls, section,file_name):
    times = []
    texts = []
    for t in cosine[:k]:
        text = timestamps_ls[t[1]][1]
        time = timestamps_ls[t[1]][0]
        times.append(time)
        texts.append(text)
        dictionary = {file_name:section}
        dictionary['Trancription'] = [{'time': times_sp, 'text': trans_te} for times_sp, trans_te in zip(times, texts)]

    with open('./jsonfiles/' + file_name +'.json', 'w') as fout:
        json.dump(dictionary , fout)