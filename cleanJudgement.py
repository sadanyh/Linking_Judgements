import string
import re
import sys


import nltk
nltk.download('stopwords')
# import nltk
# from nltk.corpus import stopwords

# nltk.download('stopwords')
# nltk.download('punkt')

class cleanj:

    def __init__(self, doc):
        self.doc= doc
    
    def remove_nonunicode(self,text):
        return ''.join([i if ord(i) < 128 else ' ' for i in text])

    def preprocessDoc(self):
        with open(self.doc, 'r', encoding='utf-8') as f:
            judgement = f.read()
        segments = re.split("\n(?=[0-9])",judgement)
        cleaned_segs = [r for r in segments if  r[0].isnumeric()]
                
        return cleaned_segs
