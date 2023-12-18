from nltk.corpus import stopwords
import nltk
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
#import spacy
#from spacy.cli.download import download as spacy_download


#spacyDocument = spacy.load('en_core_web_sm')
similarityMatrix = [[]]

def ComputeSimilarityBetweenChapters(chapterList_tfidf):
    similarityMatrix = cosine_similarity(chapterList_tfidf, chapterList_tfidf)
    print("Data Type of simMatrix:", similarityMatrix.dtype)
    print("Minimum Value in simMatrix:", np.min(similarityMatrix))
    print("Maximum Value in simMatrix:", np.max(similarityMatrix))
    return similarityMatrix