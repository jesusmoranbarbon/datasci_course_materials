import json
import sys
from collections import OrderedDict


def main():
    #Open the files
    tweet_file = open(sys.argv[1])

    
    #Create a dictionary of hashtag:
    #    key: hashtag
    #    value: number of appearances
    appearances = {}
    
    
    #Iterate over the tweet file
    for line in tweet_file:
        tweet = json.loads(line)
        entities = tweet.get("entities")
        if entities != None:
            hashtags = entities.get("hashtags")
            
            #Iterate hashtags for the tweets
            for key in hashtags:
                if key != None:
                    hashtag = key.get("text")
                    if  hashtag == None:
                        continue
                    
                    #Add the hashtag to the dictionary appearances
                    if appearances.get(hashtag) == None:
                        appearances[hashtag] = 1
                    else:
                        appearances[hashtag] = appearances[hashtag] + 1
    
    #Sort the dictionary in decrease order
    appearances_sort_by_value = OrderedDict(sorted(appearances.items(), key=lambda x: x[1], reverse=True))
    
    #Print the first "num" elements
    num = 10
    i=0
    for key in appearances_sort_by_value.keys():
        print key + "\t" + str(appearances_sort_by_value[key])
        i += 1
        if i == num:
            break   
    
       
    #Close the files
    tweet_file.close()



if __name__ == '__main__':
    main()
