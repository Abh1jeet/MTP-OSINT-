#will combine given no. of neutral positive and negative tweet to one file


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


outputFile="/home/abhijeet/Documents/MTP/data/JsonTotext/classfiy/combine3.txt"
target=open(outputFile,"w")
NoOfLines=500


#for negative
filePath="/home/abhijeet/Documents/MTP/data/JsonTotext/classfiy/negative.txt"

df=pd.read_csv(filePath,header=None,skiprows=0,delimiter="\t")
rows,columns=df.shape

print(rows)
print(columns)


for i in range(0,NoOfLines):
	target.write(str(df[0][i]))
	target.write('\t')
	target.write(str(df[1][i]))
	target.write('\t')
	target.write(str(df[2][i]))
	target.write('\t')
	target.write(str("negative"))
	target.write('\n')

#for positive
filePath="/home/abhijeet/Documents/MTP/data/JsonTotext/classfiy/positive.txt"

df=pd.read_csv(filePath,header=None,skiprows=0,delimiter="\t")
rows,columns=df.shape

print(rows)
print(columns)



for i in range(0,NoOfLines):
	target.write(str(df[0][i]))
	target.write('\t')
	target.write(str(df[1][i]))
	target.write('\t')
	target.write(str(df[2][i]))
	target.write('\t')
	target.write(str("positive"))
	target.write('\n')

#for neutral
filePath="/home/abhijeet/Documents/MTP/data/JsonTotext/classfiy/neutral.txt"

df=pd.read_csv(filePath,header=None,skiprows=0,delimiter="\t",engine='python',quotechar='"', error_bad_lines=False)
rows,columns=df.shape

print(rows)
print(columns)



for i in range(0,NoOfLines):
	target.write(str(df[0][i]))
	target.write('\t')
	target.write(str(df[1][i]))
	target.write('\t')
	target.write(str(df[2][i]))
	target.write('\t')
	target.write(str("neutral"))
	target.write('\n')




