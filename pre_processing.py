import string
import re
# 1. Merge words that are split by a line break

# 2. Divide the text into chapters and delete the content before chapter 1

# 3. In each chapter remove unwanted content like punctuations, numbers
# and other unwanted charaters from the text and decapitalise the remaining text.
# NOTE: replace the various characters with white spaces as come characters are spliting
#   two words and replacing those characters with nothing will cause these words to be joint into one.

# 4. Remove the extra spaces formed in the previous step, these spaces could be between words or
# in the beginning of the sentance.


def mergeWordsSplitIntoDifferentLines(text:str) -> str:
    # To find and join broker words (broken due to not
    # enough space in the line) we will find and delete
    # "-\n*", this should join the the two words but will
    # also join the two lines corresponding to the word.

    characterToDelete = r"-\n*|"
    text = re.sub(characterToDelete, "", text)
    return text

def splitChapters(text:str) -> list:
    # To remove unwanted spaces after the first letter of
    # every new chapter, we will first find all the "Chapter x"
    # or "Chapter xx" and replace them with "////////", then
    # we can use the split function of the string class to 
    # split the chapters into a list of chapters.

    chapters = r"Chapter [0-9]{1,2}\n"
    replacedText = re.sub(chapters, "////////", text)

    # Splitting the text by "////////" to form a list

    listOfChapters = replacedText.split("////////")
    
    # This removes everything befre the chapter 1 (preface, about author, etc)

    listOfChapters.pop(0)

    return listOfChapters

def removeExtraSpaces(text:str) -> str:
    # Remove spaces in the beginning of thr 
    startingSpaces = r"\n[ ]+"
    text = re.sub(startingSpaces, "\n", text)

    twoOrMoreSpaces = r"[ ]+"
    text = re.sub(twoOrMoreSpaces, " ", text)

    emptyLines = r"^\n"
    text = re.sub(emptyLines, "", text)
    return text

def removeUnwantedContentAndDecapitalize(text:str) -> str:
    regex = r".*Pride and Prejudice.*"
    text = re.sub(regex, "", text)

    regex = r".*Free eBooks at Planet eBook\.com.*"
    text = re.sub(regex, "", text)

    text = text.lower()

    regex = r"[^a-z \n]"
    text = re.sub(regex, "", text)
    return text



def runPreprocessing(text:str) -> list:
    text = mergeWordsSplitIntoDifferentLines(text)
    chaptersList = splitChapters(text)
    finalList = []
    for chapter in chaptersList:
        chapter = removeUnwantedContentAndDecapitalize(chapter)
        chapter = removeExtraSpaces(chapter)
        finalList.append(chapter)
    preprocessedText = ""
    preprocessedFile = open("Pride_and_Prejudice_preprocessed.txt", "w")
    preprocessedFile.flush()
    for i in finalList:
        preprocessedText = preprocessedText + i + "\n"
    preprocessedFile.write(preprocessedText)
    return finalList
