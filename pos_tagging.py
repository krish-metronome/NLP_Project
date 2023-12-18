# Import the necessary libraries
import nltk 
nltk.download('punkt') 
nltk.download('averaged_perceptron_tagger')  # Download the 'averaged_perceptron_tagger' for tagging

# this function is used to perform POS tagging on a list of tokens
def PerformPOSTagging(tokens:list):
    taggedTokens = []
    # Use the 'pos_tag' function from nltk to tag each token in 'tokens' with its part of speech
    # and add the tagged tokens to 'taggedTokens' list
    taggedTokens += nltk.pos_tag(tokens)
    return taggedTokens

# this function is used to plot the frequency distribution of the tags in 'taggedTokens'
def GetFrequencyDistributionOfTags(taggedTokens:list):
    
    # Create a frequency distribution of the tags in 'taggedTokens' using the FreqDist class of nltk
    tagFreqDistribution = nltk.FreqDist(tag for (word, tag) in taggedTokens)
    
    # Plot the frequency distribution of the 10 most common tags
    tagFreqDistribution.plot(10)
    
    # The 'tabulate' function of the FreqDist class of nltk is used to print the frequency distribution table
    tagFreqDistribution.tabulate()