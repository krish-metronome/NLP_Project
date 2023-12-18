from nltk.corpus import stopwords
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

def GenerateTF_IDF_Vectors(chapters):
    tfidf_vectorizer = TfidfVectorizer(lowercase=False)
    chapter_texts = [' '.join(chapter) for chapter in chapters]
    vecotrized_chapters = tfidf_vectorizer.fit_transform(chapter_texts)
    return vecotrized_chapters