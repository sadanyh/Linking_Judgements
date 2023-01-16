# Create a cosine similarity funciton

import math
import json
import numpy as np
from numpy import dot
from numpy.linalg import norm



def calculate_cosine_similarity(a, b):    
    cos_sim = dot(a,b) / (norm(a)*norm(b))
    return cos_sim
    
# function to calculate similarity between the judgement section and the relevant transcripts and add the index of the timestamp

def get_cosine_simlarity(judgement_embedding,timestamps_embeddings):
    """
    Method to get the similarity scores along with the timestamp index
    param judgement_embedding: embeddings of the judgement section (list/numpy.ndarray)
    param timestamps_embeddings: list of timestamp embeddings relevant to section (list of lists/numpy.ndarrays) 
    """    
    try:
      CS = []
      for em in timestamps_embeddings:
          CS.append((calculate_cosine_similarity(judgement_embedding,em),timestamps_embeddings.index(em)))
    except ValueError:
      CS = []
      timestamps_embeddings = [list(x) for x in timestamps_embeddings]
      for em in timestamps_embeddings:
          CS.append((calculate_cosine_similarity(judgement_embedding,em),timestamps_embeddings.index(em)))
    CS = sorted(CS, reverse=True)
    return CS

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