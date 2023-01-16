from flair.embeddings import WordEmbeddings, DocumentPoolEmbeddings,DocumentRNNEmbeddings
from flair.data import Sentence


class embeddDoc:

  glove_embedding = WordEmbeddings('glove')

# initialize the document embeddings, mode = mean, min, max
  document_embeddings = DocumentPoolEmbeddings([glove_embedding])
  document_embeddings_min = DocumentPoolEmbeddings([glove_embedding],  pooling='min')
  document_embeddings_max = DocumentPoolEmbeddings([glove_embedding],  pooling='max')
  document_embeddings_rnn = DocumentRNNEmbeddings([glove_embedding])
  """
  Class that takes the corpus of the judgement and the timestamps and returns embeddings corpus with pooling
  """
  def __init__(self, section,timestamps):
    self.section = section
    self.timestamps = timestamps
    
  def get_embeddings_mean(self):
    """
    Method that takes the corpus of section and timestamps and returns mean pooling of embeddings
    """
    section_embeddings = []
    section =  Sentence(self.section)
    self.document_embeddings.embed(section)
    section_embeddings.append(section.embedding.numpy())
    
    timestamps_embeddings = []    
    for s in self.timestamps:
      sentence = Sentence(s)
      self.document_embeddings.embed(sentence)
      timestamps_embeddings.append(sentence.embedding.numpy())
    return section_embeddings[0], timestamps_embeddings

  def get_embeddings_min(self):
    """
    Method that takes the corpus of section and timestamps and returns min pooling of embeddings
    """
    # document_embeddings_min = DocumentPoolEmbeddings([glove_embedding],  pooling='min')
    section_embeddings = []
    section =  Sentence(self.section)
    self.document_embeddings_min.embed(section)
    section_embeddings.append(section.embedding.numpy())
    
    timestamps_embeddings = []    
    for s in self.timestamps:
      sentence = Sentence(s)
      self.document_embeddings_min.embed(sentence)
      timestamps_embeddings.append(sentence.embedding.numpy())
    return section_embeddings[0], timestamps_embeddings
  def get_embeddings_max(self):
    """
    Method that takes the corpus of section and timestamps and returns max pooling of embeddings
    """
    # document_embeddings_min = DocumentPoolEmbeddings([glove_embedding],  pooling='min')
    section_embeddings = []
    section =  Sentence(self.section)
    self.document_embeddings_max.embed(section)
    section_embeddings.append(section.embedding.numpy())
    
    timestamps_embeddings = []    
    for s in self.timestamps:
      sentence = Sentence(s)
      self.document_embeddings_max.embed(sentence)
      timestamps_embeddings.append(sentence.embedding.numpy())
    return section_embeddings[0], timestamps_embeddings

  def get_embeddings_rnn(self):
    """
    Method that takes the corpus of section and timestamps and returns max pooling of embeddings
    """
    # document_embeddings_min = DocumentPoolEmbeddings([glove_embedding],  pooling='min')
    section =  Sentence(self.section)
    self.document_embeddings_rnn.embed(section)
    sent_emeddding = section.embedding
    
    timestamps_embeddings = []    
    for s in self.timestamps:
      sentence = Sentence(s)
      self.document_embeddings_rnn.embed(sentence)
      timestamps_embeddings.append(sentence.get_embedding())
    return sent_emeddding, timestamps_embeddings

    