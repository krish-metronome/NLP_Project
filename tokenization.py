# Import and download the necessary libraries
import nltk
nltk.download('punkt')

# This function is used to tokenize the input text
def runTokenization(text:str):
    # Use the pre-defined 'word_tokenize' function from nltk to tokenize the input text into words
    return nltk.tokenize.word_tokenize(text)