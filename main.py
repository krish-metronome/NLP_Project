#project round -1 below
# Import necessary modules and functions from all the other modules
from pre_processing import runPreprocessing
from tokenization import runTokenization
from stop_words_removal import removeStopWords
from freq_distribution_of_tokens import GetFrequencyDistribution, VisualiseFrequencyDistribution, CreateWordCloud
from pos_tagging import PerformPOSTagging, GetFrequencyDistributionOfTags
import random
from bigram_modelling import generateBigrams, CreateBigramProbabilityTable
from shannon_game import CreateBlanksForShannonGame, PlayingTheShannonGame
from tf_idf_vectors import GenerateTF_IDF_Vectors
from chapter_similarity import ComputeSimilarityBetweenChapters
from similarity_visualisation import VisualiseSimilarity
from named_entity_recognition import performNERonEntireText, extractNERTagsFromRandomPassage
from performance_evaluation_and_visualisation import evaluatePerformance, visualisePerformanceUsingBarPlots, visualisePerformanceUsingConfusionMatrix

# Import all the content of the selected book and open it in read mode 
orignalFile = open('Pride_and_Prejudice.txt', 'r')
content = orignalFile.read()

# Run preprocessing on the content to prepare NLP ready data
preprocessedTextChapters = runPreprocessing(content)

# Combine preprocessed chapters into a single string data structure
preprocessedText= ""
for i in preprocessedTextChapters:
    preprocessedText = preprocessedText + i + "\n"

# Tokenize the preprocessed text 
tokenizedText = runTokenization(preprocessedText)

# Remove stopwords from the tokenized text
tokenisedTextWithoutStopwords = removeStopWords(tokenizedText)

# Print and visualize the frequency distribution of tokens using BarGraphs and Frequency Distributions
tokenFD = GetFrequencyDistribution(tokenisedTextWithoutStopwords)
VisualiseFrequencyDistribution(tokenFD)

# Create a word cloud from the tokenized text to visualise its frequency distribution
CreateWordCloud(tokenisedTextWithoutStopwords)

# Perform Part-of-Speech (POS) tagging on the tokenized text using the default penn-treebank tagset 
taggedTokens = PerformPOSTagging(tokenisedTextWithoutStopwords)

#Analysing the frequency distrinution of the most frequent tags using plots
GetFrequencyDistributionOfTags(taggedTokens)

# Randomly select 10 chapters for the bigram model training set and merge them into a sinlge string of text
randomChapterIndexes = random.sample(range(1, len(preprocessedTextChapters)), 10)
trainingSetForBigramModel = ""
for chapterNumber in randomChapterIndexes:
    trainingSetForBigramModel += preprocessedTextChapters[chapterNumber]

# Tokenize the training set for bigram modeling without removing the stop words 
trainingSetForBigramModel = runTokenization(trainingSetForBigramModel)

# Generate bigrams from the training set
bigrams = generateBigrams(trainingSetForBigramModel)

# Create and print a bigram probability table
bigramProbabiltyTable = CreateBigramProbabilityTable(bigrams, trainingSetForBigramModel)

# Extract distinct tokens from the training set useful in the shannon game module
distinct_tokens = list(set(sorted(trainingSetForBigramModel)))

preprocessedTextChaptersForTesting = []
# Iterate through chapters and add chapters not in the training set to the list
for chapterNumber in range(len(preprocessedTextChapters)):
    if chapterNumber not in randomChapterIndexes:
        preprocessedTextChaptersForTesting.append(preprocessedTextChapters[chapterNumber])

# Randomly select a test chapter from the chapters not used in training
testPreprocessedTextChapter = random.choice(preprocessedTextChaptersForTesting)

# Tokenize the test chapter for the Shannon game
testTokenSetForShannonGame = runTokenization(testPreprocessedTextChapter)

# Create blanks in the test token set for the Shannon game and store original tokens that the blanks replaced
testTokenSetWithBlanks, originalTokens = CreateBlanksForShannonGame(testTokenSetForShannonGame, 50)

# Play the Shannon game with the test token set and get the accuracy of the bigram model trained above
PlayingTheShannonGame(testTokenSetWithBlanks, bigramProbabiltyTable, 50, distinct_tokens, originalTokens)

#Round-2 code below
#Implementing the part-2 of round-2 first

#part-2 below
# Tokenizing all the chapters to prepare them for the tf_idf vectorization
# although the tf_idf vectorizer has a built in tokenizer, we will use our custom function instead
tokenisedChapters = [runTokenization(chapter) for chapter in preprocessedTextChapters]
tokenisedChaptersWithoutStopwords = [removeStopWords(ChapterTokens) for ChapterTokens in tokenisedChapters]

#Vectorise each chapter to make tf_idf vectors
chapterVectors = GenerateTF_IDF_Vectors(tokenisedChaptersWithoutStopwords)
print("TF_IDF matrix generated for the chapters:")
print(" ")
print(chapterVectors)

#Calculating Similarity between chapters using cosine similiarity 
similarityScoresMatrix = ComputeSimilarityBetweenChapters(chapterVectors)
print("Similarity matrix showing the similarity between chapters:")
print(" ")
print(similarityScoresMatrix)

#visualise similarity using heat map
VisualiseSimilarity(similarityScoresMatrix, tokenisedChaptersWithoutStopwords)


# part-1 below
performNERonEntireText(preprocessedText)

#iteration-1
passage1 = preprocessedText[0: 1000]
passage2 = preprocessedText[2000: 3000]
passage3 = preprocessedText[4000: 5000]
passage = passage1 + passage2 + passage3
predicted_labels = extractNERTagsFromRandomPassage(passage)
print(predicted_labels)
manual_labels = ['ORDINAL', 'LOC', 'PERSON', 'DATE', 'LOC', 'GPE', 'DATE', 'PERSON', 'CARDINAL', 'CARDINAL', 'GPE', 'GPE', 'CARDINAL', 'CARDINAL', 'TIME', 'ORDINAL', 'PERSON', 'PERSON', 'PERSON', 'PERSON']
evaluatePerformance(predicted_labels, manual_labels)
visualisePerformanceUsingConfusionMatrix(predicted_labels, manual_labels)
visualisePerformanceUsingBarPlots(predicted_labels, manual_labels)


#iteration-2
passage4 = preprocessedText[6000: 7000]
passage5 = preprocessedText[8000: 9000]
passage6 = preprocessedText[10000: 11000]
passage = passage4 + passage5 + passage6
predicted_labels = extractNERTagsFromRandomPassage(passage)
print(predicted_labels)

manual_labels = ['PERSON', 'PERSON', 'PERSON', 'TIME', 'PERSON', 'DATE', 'PERSON', 'CARDINAL', 'PERSON', 'PERSON', 'GPE', 'ORDINAL', 'CARDINAL', 'CARDINAL', 'PERSON', 'ORG', 'TIME', 'MONEY']
evaluatePerformance(predicted_labels, manual_labels)
visualisePerformanceUsingConfusionMatrix(predicted_labels, manual_labels)
visualisePerformanceUsingBarPlots(predicted_labels, manual_labels)


#iteration-3
passage7 = preprocessedText[12000: 13000]
passage8 = preprocessedText[14000: 15000]
passage9 = preprocessedText[16000: 17000]
passage = passage7 + passage8 + passage9
predicted_labels = extractNERTagsFromRandomPassage(passage)
print(predicted_labels)
manual_labels = ['PERSON', 'TIME', 'PERSON', 'PERSON', 'ORG', 'PERSON', 'PERSON', 'CARDINAL', 'EVENT']
evaluatePerformance(predicted_labels, manual_labels)
visualisePerformanceUsingConfusionMatrix(predicted_labels, manual_labels)
visualisePerformanceUsingBarPlots(predicted_labels, manual_labels)
