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


#This function receices a string phrase and a total score of the prhase.
#The function iterate the words of phrase and if a word does not in the scores
#dictionary then in the position word of the dictionary new_words adds the score
#of its tweet
def add_score_new_words(phrase, score):
    words=phrase.split()
    for w in words:
        if scores.get(w)==None:
            if new_words.get(w)==None:
                new_words[w]=int(0)
            else:
                new_words[w]=new_words[w]+score


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

    #Create a dictionary who contains the new words with the sum of puntualizations
    #of the total tweets when its appear
    #Now, the dictionary is empty
    global new_words
    new_words= {}

    #Iterate over the tweet file
    for line in tweet_file:
       tweet=json.loads(line)
       text=tweet.get("text")
       if text!=None:
         tweet_score = score_per_phrase(text)
         add_score_new_words(text, tweet_score)

    #Print the new_words with its puntualizations
    for k in new_words.keys():
       print k+"\t"+str(new_words.get(k))

    #Close the files
    sent_file.close()
    tweet_file.close()



if __name__ == '__main__':
    main()
