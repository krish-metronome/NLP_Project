# Import the 'stopwords' corpus from nltk and the nltk library
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

# This function is used to remove the stopwords from a list of tokens
def removeStopWords(tokens:list):
    # Set the stop_words as the deafult english stopwords pre-defined in NLTK
    stop_words = set(stopwords.words('english'))
    
    # Create and return a new list called 'finalList' that contains all the tokens that are not stop_words
    finalList = [word for word in tokens if word not in stop_words]
    return finalList