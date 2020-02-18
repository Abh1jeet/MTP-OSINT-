import pandas as pd 
import numpy as np 
import re
import json
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split

import nltk
filePath="/home/abhijeet/Documents/MTP/data/randomData/matrix_test1_neg"

df=pd.read_csv(filePath,header=None,skiprows=0,delimiter="\t")
rows,columns=df.shape

print(rows)
print(columns)

outputFile="/home/abhijeet/Documents/MTP/data/JsonTotext/combineMatrix.txt"
target=open(outputFile,"w")


for i in range(0,rows):
	target.write(str(df[0][i]))
	target.write('\t')
	target.write(str("negative"))
	target.write('\n')




filePath="/home/abhijeet/Documents/MTP/data/randomData/matrix_test1_neu"

df=pd.read_csv(filePath,header=None,skiprows=0,delimiter="\t")
rows,columns=df.shape


for i in range(0,rows):
	target.write(str(df[0][i]))
	target.write('\t')
	target.write(str("neutral"))
	target.write('\n')

print(rows)
print(columns)

filePath="/home/abhijeet/Documents/MTP/data/randomData/matrix_test1_pos"

df=pd.read_csv(filePath,header=None,skiprows=0,delimiter="\t")
rows,columns=df.shape


for i in range(0,rows):
	target.write(str(df[0][i]))
	target.write('\t')
	target.write(str("positive"))
	target.write('\n')

print(rows)
print(columns)
