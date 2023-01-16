import cleanJudgement as cj
import segementJudgement as sg
import keywordExtraction as key

# cleaning the judgement
judge= cj.cleanj('judgement.txt')
clean_judge = judge.preprocessDoc()
# print(clean_judge)

# # segmenting the judgement 
# #into paragraphs

# judge_all = sg.segmentJ(clean_judge, paragraphs=True)
# paragraphs = judge_all.paras()
# # print(paragraphs[1])
# # print('--------------------------------')

# #into sections as per the judgement hard-coded sections

section_names = ['Summary','The background','The facts of this case','Preserving the status quo','Conclusions in principle',' The Outcome in this Case']
judge_all = sg.segmentJ(clean_judge, paragraphs=False)
secs = judge_all.sections(section_names)
summary = secs[0]
text_summary = ''.join(secs[0])
# print(text_summary)


#extract both quoted keywords and BLACKSTONE NEs from judgement sections
# The Summary list
extractor = key.extractkeywords()
summary_quotes = extractor.quotes_extract(secs[0])
full_list_summary = extractor.create_NE_lists('summary.csv',summary_quotes)
# print(full_list_summary)

#Timestamp preprocessing

import timestampExraction as ts

transcript = ts.timestamp('transcripts.txt')
clean_transcript = transcript.segment()
# print(clean_transcript)
long_timestamps = transcript.longTimestamps(clean_transcript)
#print(len(long_timestamps))
summary_timestamps = transcript.extractTimestamps(long_timestamps,full_list_summary )
# print(len(summary_timestamps))
text_timestamp_summary = transcript.getText(summary_timestamps)
# print(text_timestamp_summary[0])

from featureExtraction.tfidf import tf_idf_similarity

print(tf_idf_similarity(text_summary,text_timestamp_summary))


