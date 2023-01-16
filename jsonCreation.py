import re
import json



def add_keyword_tag(ents_list,text):
    """ Method takes a list of NEs and a text and returns a tagged text:
    :param ent_list: list of entities (str)
    :param text: text judgement or transcript (str)
    """
    KEYWORD_PRE = '<KEYWORD>'
    KEYWORD_PRE_LEN = len(KEYWORD_PRE)
    KEYWORD_POST = '</KEYWORD>'
    KEYWORD_POST_LEN = len(KEYWORD_POST)
    idx = 0
    inds = []
    for k in ents_list:
        idx = 0
        for match in re.finditer(k,text):
            text = text[:match.start()+idx] + KEYWORD_PRE + text[match.start()+idx:]
            idx += KEYWORD_PRE_LEN
            text = text[:match.end()+idx] + KEYWORD_POST + text[match.end()+idx:]
            idx += KEYWORD_POST_LEN
        
    return(text)



def add_id(section_name,section,section_ents, id):
    
    """ Takes a json file and returns a tagged text and ids to the judgement section:
    :param section_name: name of the section in json file (str)
    :param section: a list of the section of jugement (list)
    :param section_ents: a list of entities mentioned in the judgement section (list)
    :param id: the ID of the section (int)
    """
    with open(section_name + '.json') as f:
        data = json.load(f)
        #add tags to transcriptions
        for n in range(len(data['Trancription'])):
            data['Trancription'][n]['text']= add_keyword_tag(section_ents,data['Trancription'][n]['text'])
        #add tags to section of judgement
        section_all = "".join(section) #joining the sentences in the section list
        section_keyword = add_keyword_tag(section_ents,section_all)# adding keyword tag

        data[section_name] = section_keyword #changing the section in json file with clean and keywords
        # add ID
        data_id= {'judge_id': id}  # add id at the beginning of the data
        data_id.update(data)
        return data_id

def createJson(list_dictionries,filename):
    """ 
    Takes a list of dictionaries for each judgement section and creates a json file:
    :param list_dictionries: list of dictionaries (list)
    :param filename: name of file (str)
    """
    with open(filename + '.json', "w") as final:
        json.dump(list_dictionries, final)