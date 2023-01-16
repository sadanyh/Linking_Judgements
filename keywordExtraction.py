import re
from typing import List
import string
from nltk.corpus import stopwords
import pandas as pd

stop_words = set(stopwords.words('english'))

class extractkeywords:
    """
    Extractor class to create quoted keywords and NEs list
    """
    def __init__(self) -> None:
        pass
    # def __init__(self,segment: List[str]):
    #     self.segment = segment

    def quotes_extract(self, segment):
        quotes= []
        for line in segment:  
            res = re.findall(r'"(.*?)"', line)
            for r in res:
                if len(r.split()) <= 3: #get only short keywords to avoid extracting long quotations
                    quotes.append(r)
        return quotes
#function to remove stop words  

    def remove_stopwords(self,text,stop_words):
        """
            Method used to remove stopwords from the document
            :param text: Input text
            :param stop_words: Enlish stopwords (can be adapted to the case)
            :return: Cleaned document           
            """       
        output_array=[]
        for sentence in text:
            temp_list=[]
            for word in sentence.split():
                if word.lower() not in stop_words:
                    temp_list.append(word)
            output_array.append(' '.join(temp_list))
        return output_array   

    def create_NE_lists(self,file,quotes):

        """
            Method used to add the BLACKSTONE NEs of each section to the quoted keywords of each section and clean the whole list
            :param file: Input blackstone file containing NE list
            :param quotes: Input list of quoted keywords
            :return: Cleaned entity list
            """
        data = pd.read_csv(file, encoding='utf8')
        ents =  [re.sub("\s\s+" , " ", ent) for ent in data['Word'].to_list()]  #clean extra spaces
        printable = set(string.printable) #clean non-utf8
        ents = ["".join(filter(lambda c: c in printable, ent)) for ent in ents]
        new_ents = list(dict.fromkeys(ents)) #delete duplicates
        new_ents = self.remove_stopwords(new_ents,stop_words) #clean stopwords
        new_ents = [elem for elem in new_ents if len(elem) > 10] #excluse short NEs
        new_ents = [re.sub("\[\d+\]\s+" , "", ent) for ent in new_ents] #take the year out of the case names
        new_ents = new_ents+quotes+[('"'+t+'"') for t in quotes ] #add quoted quotes
        return new_ents


  