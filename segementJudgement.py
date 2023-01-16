from typing import List


class segmentJ(object):
    """
       Segment the judgement as per the human sections or the digit paragraphs
    """
    def __init__(self, doc: List[str],  paragraphs: bool = False):

            """
            :param doc: cleaned judgement list of strings
            :param paragraphs: whether to segement per paragraph or per section
            """
            self.doc = doc
            
            self.paragraphs= paragraphs

    def paras(self):
        """Method to segment the judgement by paragraph"""
        if self.paragraphs:
            segments = [line for line in self.doc if line[0].isdigit()]
        return segments

    def sections(self, sections):
        """Method to segment the judgement by section
        param sections: a hard-coded section list extracted from judgement
        """
        inds = []
        segments = []
        for line in self.doc:
            for sec in sections:
                if sec in line:
                    inds.append(self.doc.index(line))
        
        for i in range(len(inds)-1):
            segments.append(self.doc[inds[i]:inds[i+1]])
        segments.append(self.doc[inds[-1]:])
        
        return segments


               



