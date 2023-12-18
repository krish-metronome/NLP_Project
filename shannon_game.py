#import the necessary libraries
import nltk
import random
import sys # For system-specific parameters and functions

# This function will create random blanks in the provided text chapter to create the shannon game problem
def CreateBlanksForShannonGame(tokens:list, num_blanks:int):
    blank_positions = random.sample(range(1, len(tokens)), num_blanks) # Generate random indexes for blanks
    blank_positions.sort() # Sort the indexes in ascending order so as to enable comparing the original tokens with the tokens with blanks later
    originalTokens = []
    for i in blank_positions: # Replace the tokens at the randomly generated indexes with blanks after storing them
        originalTokens.append(tokens[i])
        tokens[i] = "_"
    return tokens, originalTokens

# This function will play the shannon game with the provided text chapter and the trained bigram model
def PlayingTheShannonGame(tokens: list, bigramProbabilityTable, num_blanks, distinct_tokens: list, originalTokens):
    ogTokenIndex = -1 # This will be used to keep track such that the blank is compared with original token that it replaced
    correctlyFilledBlanks = num_blanks # we start with the assumption that all blanks are filled correctly

    for i in range(len(tokens)): # Iterate through the entire chapter
        if(tokens[i] == "_"): # If a blank is encountered

            #increase this index to represent the 1st token(index = 0) in the original tokens list
            #that will be compared with the first blank, this will increase at every blank encountered
            ogTokenIndex += 1 
            try:
                previousWordIndex = i - 1 # Get the index of the previous word since we are using bigrams
                maxProb = -sys.maxsize + 1 # Initialise the maximum probability to a very small number

                # Get the index of the token that has the maximum probability of occuring after the previous word
                # we will achieve this by first finding the index of list that contains the bigrams starting with the previous word
                # and then finding the index of the bigram with the maximum probability in that list
                list_index = distinct_tokens.index(tokens[previousWordIndex])
                for prob in bigramProbabilityTable[list_index]:
                    maxProb = max(prob, maxProb)
                indexOfTokenToBeReplaced = bigramProbabilityTable[list_index].index(maxProb)

                # we finally check if the filled word is the same as the original word that was replaced
                # if not, we decrease the number of correctly filled blanks
                if(distinct_tokens[indexOfTokenToBeReplaced] != originalTokens[ogTokenIndex]):
                    correctlyFilledBlanks -= 1
            except:
                correctlyFilledBlanks -= 1         
    # Call the function to get the performance of the bigram model  
    GetPerformanceOfBigramModel(correctlyFilledBlanks, num_blanks) 


# This function will print the accuracy of the bigram model
def GetPerformanceOfBigramModel(correctlyFilledBlanks, num_blanks):

    # Calculate the accuracy of the bigram model by dividing the number of correctly filled blanks by the total number of blanks
    # and print the accuracy
    accuracyOfModel = (correctlyFilledBlanks / num_blanks) * 100
    print("Accuracy of the bigram model generated is: ")
    print(accuracyOfModel)