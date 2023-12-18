#import necessary libraries
import nltk
import random # For generating random numbers

# This function is used to generate a list of bigrams from a list of tokens
def generateBigrams(tokens:list):

    # Use the 'ngrams' function from nltk to generate a list of bigrams from the input tokens
    tokenBigrams = nltk.ngrams(tokens, 2)  # the second parameter represents the 'n' in n-grams
    bigrams = list(tokenBigrams)
    print("\n")
    print("Total number of Bigrams: ")
    print(len(bigrams))
    print("\nSome Examples of Bigrams:\n")
    print(bigrams[:20], "......")
    return bigrams

# This function is used to create a bigram probability table from a list of bigrams generated above
def CreateBigramProbabilityTable(bigrams: list, tokens: list):
    bigramFD = nltk.FreqDist(bigrams) # Create a frequency distribution of the bigrams using the 'nltk' library
    bigramFD.plot(10) # Plot the frequency distribution of the bigrams using 'matplotlib'

    #select the 20 most common bigrams from the distribution and print them
    print("\nSome Bigram counts and frequency distribution:")
    bigramFDMostCommon = bigramFD.most_common(20)
    for bigram in bigramFDMostCommon:
        print(bigram)

    # Extract distinct tokens from the list of tokens
    # Create token and bigram dictionaries from their frequency distributions
    # Pass all the above to the function that will calculate the bigram probabilities
    distinct_tokens = list(set(sorted(tokens)))
    token_dct = dict(nltk.FreqDist(tokens))
    bigram_dct = dict(bigramFD)
    bigramProbabiltyTable = CalculateBigramProbabilities(distinct_tokens, token_dct, bigram_dct)
    return bigramProbabiltyTable


# This function is used to find wether the given bigram exists in the bigram dictionary
# If it does, it returns the count of the bigram, else it returns 0
def FindBigram(bigram : tuple, bigram_dct: dict):
    try:
        return bigram_dct[bigram]
    except:
        return 0


# This function is used to calculate the bigram probabilities
def CalculateBigramProbabilities(distinct_tokens:list, token_dct: dict, bigram_dct: dict):
    n = len(distinct_tokens) # Get the number of distinct tokens
    # Create a 2D list to store the bigram probability distribution
    bigramProbabilityDistribution = [[]*n for i in range(n)] 

    # Iterate through the distinct tokens and calculate the bigram probabilities
    for i in range(n):
        countOfPreviousWord = token_dct[distinct_tokens[i]] #Get the count/frequency of the previous word from the frequency distribubtion dictionary
        for j in range(n):
            bigram = (str(distinct_tokens[i]), str(distinct_tokens[j])) #Create a bigram tuple from the previous word and the current word
            countOfTheBigram = FindBigram(bigram, bigram_dct) #Find the count of the bigram in the bigram dictionary if it exists
           
            # Calculate the bigram probability and append it to the bigram probability distribution list
            bigramProbabilityDistribution[i].append(float("{:.3f}".format(countOfTheBigram/countOfPreviousWord)))
    return bigramProbabilityDistribution
    

