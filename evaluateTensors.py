import torch
import json


def calculate_cosine_similarity(timestamps_embeddings, sentence_embedding):
    cos = torch.nn.CosineSimilarity(dim=0)

    """Method to get the similarity scores between tensor embeddings
    param timestamps_embeddings: timestamp embeddings (list of tensors)
    param sentence_embedding: section embedding ( tensor)
    returns: a tuple list of (cosine similarity score, index in timestamps list)
    """  
    output = []
    ind= []
    for e in timestamps_embeddings:
      output.append(cos(e,sentence_embedding))
    temp = [t.detach().numpy() for t in output]
    cos_sim = [l.tolist() for l in temp]
    sorted_scores = sorted(cos_sim, reverse=True)
    
    for i in range(len(sorted_scores)):
      ind.append(cos_sim.index(sorted_scores[i]))
    return list(zip(sorted_scores,ind))

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

    with open('./jsonfiles/' + file_name +'.json', 'w') as fout:
        json.dump(dictionary , fout)