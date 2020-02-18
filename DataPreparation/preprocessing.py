## tweetText + lexiconSet ----->1 single file containing corresponding tweet and its label 

#this program will read all the files from one folder 
#and also read all the lexicons from lexicon file
#it will then distribute all the different sentiments in different dictionary
#it will then give label to the tweet if it contains all the lexicons of same type
#after that it will write tweet along with there sentiment in one file


import json
import glob



path = "/home/abhijeet/Documents/MTP/data/data1/2019-08-27"   
files = [f for f in glob.glob(path + "**/*.json", recursive=True)]

#path of the folder containing tweets
#files all the files present in the folder





#counting files in the folder
count=0
for filepath in files:
    count=count+1
print(count)



#output file will contain tweets along with there sentiment
outputFile="/home/abhijeet/Documents/MTP/data/JsonTotext/try.txt"
target=open(outputFile,"w")



#with open(outputFile, 'a+') as json_file:
















###making dictionary of positive words
positiveLexicon=set()  #contains all the positive words
negativeLexicon=set()  #contains all the negative words
neutralLexicon=set()   #contains all the neutral words



#path of file which contains all the emotion word pairs
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




#now each dictionary will contains corresponding emotion words
#for x in positiveLexicon:
    #print(x)





positiveLexicon.add("saaho")
neutralLexicon.add("purplecarpet")




for filepath in files:
    with open(filepath) as filename:
        data = json.load(filename)
        t_text=str(data["tweet_text"])   #reading only text of tweet
        t_text=t_text.replace('\n', ' ') #removing newline
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
            
            if(p+ne+n==1):#to check if tweet contains only one type of lexicon
                t_hastags=t_hastags[:-1]
                target.write(str(data["tid"]))
                target.write('\t')
                target.write(t_text)
                target.write('\t')
                target.write(t_hastags)
                target.write('\t')
                if(p==1):
                    target.write("positive")
                if(ne==1):
                    target.write("negative")
                if(n==1):
                    target.write("neutral")
                target.write('\n')


print(count)
