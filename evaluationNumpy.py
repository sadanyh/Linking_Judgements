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

  ind= []    
  cos_sim = np.dot(a,b) / (norm(a, axis=1)*norm(b))
  cos_sim = cos_sim.tolist()
  sorted_scores = sorted(cos_sim, reverse=True)
  for i in range(len(sorted_scores)):
    ind.append(cos_sim.index(sorted_scores[i]))
  return list(zip(sorted_scores,ind))

  #get index of the raw text according to similarity scores
  

# function to create a json file with the results of the cosine similarity measure
  
def get_results(cosine,k,timestamps_ls, section,file_name):

  """Method to create results in json file
  param cosine: a list of tuples of similarity scores and index (list of tuples)
  param timestamps_ls: list of timestamps with times and text ( list of strings)
  param section: text of the judgement section (str)
  param file_name: file name (str)
  returns: json file
  """  
  times = []
  texts = []
  for t in cosine[:k]:
      text = timestamps_ls[t[1]][1]
      time = timestamps_ls[t[1]][0]
      times.append(time)
      texts.append(text)
      dictionary = {file_name:section}
      dictionary['Trancription'] = [{'time': times_sp, 'text': trans_te} for times_sp, trans_te in zip(times, texts)]

  with open('./' + file_name +'.json', 'w') as fout:
      json.dump(dictionary , fout)