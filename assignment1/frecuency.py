import json
import sys


def main():
    #Open the files
    tweet_file = open(sys.argv[1])

    #Create a dictionary who contains the words with the sum of appearances
    #Now, the dictionary is empty
    global words
    words= {}

    #Iterate over the tweet file
    for line in tweet_file:
       tweet=json.loads(line)
       text=tweet.get("text")
       if text!=None:
          text_split=text.split()
          for w in text_split:
            if words.get(w)==None:
                words[w]=1
            else:
                words[w]=words[w]+1

    #Print the words with its appearances
    for k in words.keys():
       print k+"\t"+str(words.get(k))

    #Close the file
    tweet_file.close()



if __name__ == '__main__':
    main()
