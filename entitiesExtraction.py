from typing import List
import re
import spacy
from spacy import displacy
from blackstone.displacy_palette import ner_displacy_options
import en_core_web_sm
#load spacy model
spacy = en_core_web_sm.load()
# Load blackstone model. It is better to initiate first outside the class.
nlp = spacy.load("en_blackstone_proto") 

class extractEntities(object):
    
    """ A method to extract both blackstone and spaCy entites from the sections of the judgement
    """

    def __init__(self, segment: List[str]):
        
             """
            :param segment: cleaned section of the judgement list of a string
            """
        self.segment= segment
    

    def quotes_extract(self,segment):
         """
         Extract bigrams in quotations from judgement section
        :param segment: section of judgement  a list with one string
        :return: a list of quotes
        """
        quotes= []
        for line in self.segment:  
            res = re.findall(r'"(.*?)"', line)
            for r in res:
                if len(r.split()) <= 3: #get only short keywords to avoid extracting long quotations
                    quotes.append((r,'Keyword'))
        return quotes
   
    def blackstone_qoutes_nes(self):
        
        """
        Extract blackstone entities and quotes from judgement section        
        :return: a list of entities and keyword in quotes
        """
        labels = []
        text = "".join(self.segment)
        black_seg = nlp(text)
        for ent in black_seg.ents:
            labels.append((ent.text,ent.label_))
        quotes = self.quotes_extract(self.segment)
        long_list = labels+quotes
        return long_list
    
    def spacy_nes(self):
        
        """
        Extract spacy entities  from judgement section        
        :return: a list of spacy entities 
        """
        labels = []
        text = "".join(self.segment)
        spacy_ner = spacy(text)
        for ent in spacy_ner.ents:
            labels.append((ent.text,ent.label_))
        return labels

    


#     #to avoid new lines in the csv
#         with open(name + '.csv','w',newline='') as out:
#             csv_out=csv.writer(out)
#             csv_out.writerow(['Word','Label'])
#             for row in long_list:
#                 csv_out.writerow(row)
