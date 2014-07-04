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


#Return the abbreviation of the US state, or None if does not achieved
def obtain_state_abbreviation(place):
    #Create a dictionary of U.S. states abbreviations
    #source: http://code.activestate.com/recipes/577305-python-dictionary-of-us-states-and-territories/
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    
    #If the place is not established the state is invalid
    if place == None:
        return None        
        
    
    #If the country is not US then the state is invalid
    if place.get("country") != "United States":
        return None
        
     
    st_abbreviation = None
    
    #First intent to obtain the state
    full_state = place.get("full_name").split(",")[0]
    for key, value in states.iteritems():
        if value == full_state:
            st_abbreviation = key
    
    #Second intent to obtain the state
    if st_abbreviation == None:
        if place.get("full_name")[-4:-2] == ", " and place.get("full_name")[-2:].upper() != None:
            st_abbreviation = place.get("full_name")[-2:].upper()
    
    #Check if exist the abbreviation
    #If at this time the st_abbreviation is not valid, the tweet is omitted
    if states.get(st_abbreviation) == None:
        return None
    
    return st_abbreviation    



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

    #Create a dictionary who contains:
    #    key: the state (abbreviate)
    #    value: the sum of the score of sentiments
    sum_scores = {}
    
    
    #Create a dictionary who contains:
    #    key: the state (abbreviate)
    #    value: the number of scores
    total_scores = {}
    
    
    #Iterate over the tweet file
    for line in tweet_file:
        tweet=json.loads(line)
        place=tweet.get("place")
        
        #Obtain the abbreviation
        st_abbreviation = obtain_state_abbreviation(place)
        
        #If st_abbreviation is invalid then the tweet is omitted
        if st_abbreviation == None:
            continue
        
        #The tweet is omitted if does not contain text
        text = tweet.get("text")
        if text == None:
            continue
        
        #Add to the sum_scores and increment total_scores
        tweet_score = score_per_phrase(text)
        if sum_scores.get(st_abbreviation) == None:
            sum_scores[st_abbreviation] = tweet_score
            total_scores[st_abbreviation] = 1
        else:
            sum_scores[st_abbreviation] = sum_scores[st_abbreviation] + tweet_score
            total_scores[st_abbreviation] = total_scores[st_abbreviation] + 1

    
    #Calculation of the average
    averages = {}
    for key in sum_scores.keys():
        averages[key] = sum_scores[key]/total_scores[key]
        
    #Calculation of state who has the maximum score
    if len(averages.keys()) > 0:
        state_maximum_score = averages.keys()[0]
        maximum_score = averages[state_maximum_score]
        for key in averages.keys():
            if averages[key] > maximum_score:
                state_maximum_score = key
                maximum_score = averages[state_maximum_score]
    
        #Print the result
        print state_maximum_score

    #Close the files
    sent_file.close()
    tweet_file.close()



if __name__ == '__main__':
    main()
