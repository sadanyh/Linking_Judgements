class timestamp:

    def __init__(self, doc):
        self.doc= doc

    def segment(self):
        with open(self.doc, 'r', encoding='utf8') as f:
            trans= f.readlines()
            trans_lists = [t.split('"') for t in trans]
        out = []
        for ll in trans_lists:
            if ll == '\n':
                continue
            if isinstance(ll, list):
                ll = self.cleanEmptylines(ll)
                if not ll:
                    continue
            out.append(ll)
        return out

  # clean transcripts from the '\n'          
    def cleanEmptylines(self,l):     
        out = []
        for ll in l:
            if ll == '\n':
                continue
            if isinstance(ll, list):
                ll = self.cleanEmptylines(ll)
                if not ll:
                    continue
            out.append(ll)
        return out


# choose only long transcripts

    def longTimestamps(self,l):
        out = []
        for ll in l:
            try:
                if len(ll[1].split()) < 50:
                    continue
            except:
                continue
            if isinstance(ll, list):
                ll = self.cleanEmptylines(ll)
                if not ll:
                    continue
            out.append(ll)
        return out
            
# a function to extract timestams that contain quoted keywords and NEs in each section of the judgement

    def extractTimestamps(self,timestamp_list, section_keywords):
        timestamps = []
        for sent in timestamp_list:
            for keyword in section_keywords:
                if keyword in sent[1]:
                    timestamps.append(sent)
        new_timstamps = []
        for elem in timestamps:
            if elem not in new_timstamps:
                new_timstamps.append(elem)        
        return new_timstamps

    def getText(self, timestamplist):
        trans_summary_corpus =[sent[1] for sent in timestamplist]
        return trans_summary_corpus
    
   