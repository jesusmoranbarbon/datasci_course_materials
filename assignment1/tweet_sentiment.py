import json
import sys


#This function receives a string phrase, splits in words and calculates the total score
def score_per_phrase(phrase):
    words=phrase.split()
    score=0
    for w in words:
        if scores.get(w)==None:
            score+=0
        else:
            score+=scores.get(w)
    return score


def main():
    #Open the files
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    #Create a dictonary who contain the word and their score
    global scores
    scores = {} # initialize an empty dictionary
    for line in sent_file:
       term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
       scores[term] = int(score)  # Convert the score to an integer.

    #Iterate over the tweet file
    for line in tweet_file:
       tweet=json.loads(line)
       text=tweet.get("text")
       if text!=None:
         print score_per_phrase(text)


    #Close the files
    sent_file.close()
    tweet_file.close()



if __name__ == '__main__':
    main()
