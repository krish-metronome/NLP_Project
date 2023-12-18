from nltk.corpus import stopwords
import nltk
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx

def VisualiseSimilarity(simMatrix, chapters):
    #Create dataframe to visualise the matrix
    chapterNo = [f"Chapter {i+1}" for i in range(len(chapters))]
    simMatrix_df = pd.DataFrame(simMatrix, columns = chapterNo, index = chapterNo)
    
    #creating the gradient table
    sns.set(style='white')
    plt.figure(figsize=(48, 36))
    sns.heatmap(simMatrix_df,annot=True, cmap='YlGnBu')
    plt.title("Chapter-wise Cosine Similarity through Gradient Table")
    plt.show()



