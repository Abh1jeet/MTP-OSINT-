## tweetText + lexiconSet ----->3 different files containing corresponding tweet and its label 


#this program will read all the files from one folder 
#and also read all the lexicons from lexicon file
#it will then distribute all the different sentiments in different dictionary
#it will then give label to the tweet if it contains all the lexicons of same type
#after that it will write all the positive tweet in one file negative in one and neutral file


import json
import glob
path = "/home/abhijeet/Documents/MTP/data/data1/2019-08-29"   
files = [f for f in glob.glob(path + "**/*.json", recursive=True)]

count=0
for filepath in files:
    count=count+1

print(count)


outputFileNegative="/home/abhijeet/Documents/MTP/data/JsonTotext/negative.txt"
outputFilePositive="/home/abhijeet/Documents/MTP/data/JsonTotext/positive.txt"
outputFileNeutral="/home/abhijeet/Documents/MTP/data/JsonTotext/neutral.txt"

targetNegative=open(outputFileNegative,"a+")
targetPositive=open(outputFilePositive,"a+")
targetNeutral=open(outputFileNeutral,"a+")
#with open(outputFile, 'a+') as json_file:






#31 28 29









###making dictionary of positve words
positiveLexicon=set()
negativeLexicon=set()
neutralLexicon=set()

lexiconPath="/home/abhijeet/Documents/MTP/data/data1/lexicon/senti_emo_words_final"
with open(lexiconPath) as f:
   for line in f:
       values = line.split("\t")
       if(values[1]=="positive\n"):
        positiveLexicon.add(values[0])
       if(values[1]=="negative\n"):
        negativeLexicon.add(values[0])
       if(values[1]=="neutral\n"):
        neutralLexicon.add(values[0])

#for x in positiveLexicon:
    #print(x)



positiveLexicon.add("saaho")
neutralLexicon.add("purplecarpet")




for filepath in files:
    with open(filepath) as filename:
        data = json.load(filename)
        t_text=str(data["tweet_text"])
        t_text=t_text.replace('\n', ' ')
        t_hastags=""
    
        if(data["hashtags"]!=None):                 #tweet with no hastags are not required
            p=0
            ne=0
            n=0
            f=-1
            for hashtag in data["hashtags"]:
                hashtag=hashtag.lower()
                if(hashtag in positiveLexicon ):
                    p=1
                if(hashtag in negativeLexicon ):
                    ne=1
                if(hashtag in neutralLexicon ):
                    n=1
                t_hastags+=hashtag
                t_hastags+=","
            
            if(p+ne+n==1):
                t_hastags=t_hastags[:-1]
                if(p==1):
                    targetPositive.write(str(data["tid"]))
                    targetPositive.write('\t')
                    targetPositive.write(t_text)
                    targetPositive.write('\t')
                    targetPositive.write(t_hastags)
                    targetPositive.write('\t')
                    targetPositive.write("positive")
                    targetPositive.write('\n')
                if(ne==1):
                    targetNegative.write(str(data["tid"]))
                    targetNegative.write('\t')
                    targetNegative.write(t_text)
                    targetNegative.write('\t')
                    targetNegative.write(t_hastags)
                    targetNegative.write('\t')
                    targetNegative.write("negative")
                    targetNegative.write('\n')
                if(n==1):
                    targetNeutral.write(str(data["tid"]))
                    targetNeutral.write('\t')
                    targetNeutral.write(t_text)
                    targetNeutral.write('\t')
                    targetNeutral.write(t_hastags)
                    targetNeutral.write('\t')
                    targetNeutral.write("neutral")
                    targetNeutral.write('\n')


print(count)
