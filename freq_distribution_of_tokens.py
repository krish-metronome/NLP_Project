#import all the necessary libraries
from wordcloud import WordCloud, STOPWORDS # To create wordclouds
import nltk
import pandas # To analyse and manipulate data
import seaborn # To visualise data
import matplotlib.pyplot as plt # To create plots


def GetFrequencyDistribution(tokens:list):
    TokenFD = nltk.FreqDist(tokens) # Create a frequency distribution of the tokens using the FreqDist class of nltk
    return TokenFD
    
def VisualiseFrequencyDistribution(tokenFD):
    mostCommonFdist = tokenFD.most_common(20) #select the 20 most common tokens from the distribution
    mostCommonFdist = pandas.Series(dict(mostCommonFdist)) #convert the most common tokens into a pandas series

    #plot the frequency distribution of the 20 most common tokens using 'matplotlib' and 'seaborn'
    figure, ax = plt.subplots(figsize = (10,10))
    freqDistribution_plot = seaborn.barplot(x = mostCommonFdist.index, y = mostCommonFdist.values, ax = ax)
    plt.xticks(rotation = 30)

def CreateWordCloud(tokens:list):
    wordString = ""
    wordString += " ".join(tokens)+" " # Create a string of all the tokens in the list 'tokens'

    # Create a wordcloud from the wordString generated above using the WordCloud class of wordcloud library
    wordcloud = WordCloud(width = 800, height = 800, background_color = 'white', min_font_size = 10).generate(wordString)
    
    # Display the wordcloud while setting attributes such as size, background color and padding
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()






