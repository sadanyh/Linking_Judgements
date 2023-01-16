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
            lines = f.read().splitlines()
        printable = set(string.printable) #clean non-utf8
        lines_cl = [self.remove_nonunicode(line) for line in lines ]
        lines2 = [ t for t in lines_cl if t != '' if t != ' ' ] #clean empty lines
        #lines3 = [ t for t in lines2 if len(t.split()) > 10 ]
        lines3 = [re.sub("\s\s+" , " ", line) for line in lines2]
        
        return lines3
