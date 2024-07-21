import json
import re
import html
import unicodedata
import datetime
from unidecode import unidecode
from langdetect import detect
import nltk
from textblob import TextBlob

# Load the dataset
with open('data/gg2013.json', 'r') as file:
    tweets = json.load(file)

# Preprocessing functions
def clean_tweet(tweet):
    tweet = html.unescape(tweet)  # Handle HTML entities
    tweet = unicodedata.normalize('NFKC', tweet)  # Normalize unicode characters
    tweet = unidecode(tweet)  # Replace non-ASCII characters
    tweet = re.sub(r'http\S+', '', tweet)  # Remove URLs
    tweet = " ".join(tweet.split())  # Normalize whitespace
    return tweet

def detect_language(tweet):
    try:
        lang = detect(tweet)
        return lang == 'en'
    except:
        return False

def preprocess_tweets(tweets):
    cleaned_tweets = [clean_tweet(tweet['text']) for tweet in tweets if detect_language(tweet['text'])]
    return cleaned_tweets

# Extraction functions
def extract_hashtags_usernames(tweet):
    hashtags = re.findall(r'#(\w+)', tweet)
    usernames = re.findall(r'@(\w+)', tweet)
    return hashtags, usernames

def parse_tweet(tweet):
    blob = TextBlob(tweet)
    entities = []
    for np in blob.noun_phrases:
        entities.append((np, 'PERSON'))
    return entities

def parse_timestamp(timestamp_ms):
    dt = datetime.datetime.fromtimestamp(int(timestamp_ms)/1000.0)
    return dt

# Main functions to identify the required components
def identify_hosts(tweets):
    hosts = set()
    for tweet in tweets:
        if re.search(r'\bhost\b', tweet, re.IGNORECASE):
            entities = parse_tweet(tweet)
            for entity in entities:
                if entity[1] == 'PERSON':
                    hosts.add(entity[0])
    return list(hosts)

def identify_awards(tweets):
    awards = set()
    for tweet in tweets:
        if re.search(r'\bbest\b', tweet, re.IGNORECASE):
            entities = parse_tweet(tweet)
            for entity in entities:
                if re.search(r'\bbest\b', entity[0], re.IGNORECASE):
                    awards.add(entity[0])
    return list(awards)

def map_presenters_to_awards(tweets, awards):
    presenters = {award: [] for award in awards}
    for tweet in tweets:
        for award in awards:
            if award.lower() in tweet.lower():
                entities = parse_tweet(tweet)
                for entity in entities:
                    if entity[1] == 'PERSON' and entity[0] not in presenters[award]:
                        presenters[award].append(entity[0])
    return presenters

def map_nominees_to_awards(tweets, awards, nominees_dict):
    nominees = {award: [] for award in awards}
    for award in awards:
        nominees[award] = nominees_dict.get(award, [])
    return nominees

def map_winners_to_awards(tweets, awards):
    winners = {award: None for award in awards}
    for tweet in tweets:
        for award in awards:
            if re.search(rf'\b{award}\b', tweet, re.IGNORECASE) and re.search(r'\bwins\b', tweet, re.IGNORECASE):
                entities = parse_tweet(tweet)
                for entity in entities:
                    if entity[1] == 'PERSON':
                        winners[award] = entity[0]
    return winners


# nominees in 2013 Golden Globe Awards from imdb
List_Awards_Nominee = {"Best Motion Picture - Drama" : ['Argo', 'Django Unchained', 'Life of Pi', 'Lincoln', 'Zero Dark Thirty'],
                       "Best Motion Picture - Musical or Comedy" : ['The Best Exotic Marigold Hotel', 'Les Misérables', 'Moonrise Kingdom', 'Salmon Fishing in the Yemen', 'Silver Linings Playbook'],
                       "Best Performance by an Actor in a Motion Picture - Drama" : ['Daniel Day-Lewis', 'Richard Gere', 'John Hawkes', 'Joaquin Phoenix', 'Denzel Washington'],
                        "Best Performance by an Actor in a Motion Picture - Musical or Comedy" : ['Jack Black', 'Bradley Cooper', 'Hugh Jackman', 'Ewan McGregor', 'Bill Murray'],
                        "Best Performance by an Actress in a Motion Picture - Drama" : ['Jessica Chastain', 'Marion Cotillard', 'Helen Mirren', 'Naomi Watts', 'Rachel Weisz'],
                        "Best Performance by an Actress in a Motion Picture - Musical or Comedy" : ['Emily Blunt', 'Judi Dench', 'Jennifer Lawrence', 'Maggie Smith', 'Meryl Streep'],
                        "Best Performance by an Actor in a Supporting Role in a Motion Picture" : ['Alan Arkin', 'Leonardo DiCaprio', 'Philip Seymour Hoffman', 'Tommy Lee Jones', 'Christoph Waltz'],
                        "Best Performance by an Actress in a Supporting Role in a Motion Picture" : ['Amy Adams', 'Sally Field', 'Anne Hathaway', 'Helen Hunt', 'Nicole Kidman'],
                        "Best Director - Motion Picture" : ['Ben Affleck', 'Kathryn Bigelow', 'Ang Lee', 'Steven Spielberg', 'Quentin Tarantino'],
                        "Best Screenplay - Motion Picture" : ['Mark Boal', 'Tony Kushner', 'David O. Russell', 'Quentin Tarantino', 'Chris Terrio'],
                        "Best Original Score - Motion Picture" : ['Mychael Danna', 'Alexandre Desplat', 'Dario Marianelli', 'Tom Tykwer, Johnny Klimek, Reinhold Heil', 'John Williams'],
                        "Best Original Song - Motion Picture" : ['For You', 'Not Running Anymore', 'Safe & Sound', 'Skyfall', 'Suddenly'],
                        "Best Foreign Language Film" : ['Amour', 'A Royal Affair', 'The Intouchables', 'Kon-Tiki', 'Rust and Bone'],
                        "Best Animated Feature Film" : ['Brave', 'Frankenweenie', 'Hotel Transylvania', 'Rise of the Guardians', 'Wreck-It Ralph'],
                        "Best Television Series - Drama" : ['Breaking Bad', 'Boardwalk Empire', 'Downton Abbey', 'Homeland', 'The Newsroom'],
                        "Best Performance by an Actress in a Television Series - Drama": ['Connie Britton', 'Glenn Close', 'Claire Danes', 'Michelle Dockery', 'Julianna Margulies'],
                        "Best Performance by an Actor in a Television Series - Drama" : ['Steve Buscemi', 'Bryan Cranston', 'Jeff Daniels', 'Jon Hamm', 'Damian Lewis'],
                        "Best Television Series - Comedy or Musical": ['The Big Bang Theory', 'Episodes',"Girls","Modern Family","Smash"],
                        "Best Performance by an Actor in a Television Series - Comedy or Musical": ['Alec Baldwin', 'Don Cheadle', 'Louis C.K.', 'Matt LeBlanc', 'Jim Parsons'],
                        "Best Performance by an Actress in a Television Series - Comedy or Musical": ['Zooey Deschanel', 'Julia Louis-Dreyfus', 'Lena Dunham', 'Tina Fey', 'Amy Poehler'],
                        "Best Mini-Series or Motion Picture Made for Television": ["Game Change","Hatfields & McCoys","The Girl","The Hour","Political Animals"],
                        "Best Performance by an Actor in a Mini-Series or Motion Picture Made for Television": ["Kevin Costner","Benedict Cumberbatch","Woody Harrelson","Toby Jones","Clive Owen"],
                        "Best Performance by an Actress in a Mini-Series or Motion Picture Made for Television": ["Nicole Kidman","Jessica Lange","Sienna Miller","Julianne Moore","Sigourney Weaver"],
                        "Best Performance by an Actor in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television": ["Max Greenfield","Ed Harris","Danny Huston","Mandy Patinkin","Eric Stonestreet"],
                        "Best Performance by an Actress in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television": ["Hayden Panettiere","Archie Panjabi","Sarah Paulson","Maggie Smith","Sofía Vergara"]
                        }

def main():
    # Preprocess tweets
    cleaned_tweets = preprocess_tweets(tweets)

    # Identify hosts
    hosts = identify_hosts(cleaned_tweets)

    # Identify awards
    awards = identify_awards(cleaned_tweets)

    # Map presenters to awards
    presenters = map_presenters_to_awards(cleaned_tweets, awards)

    # Map nominees to awards
    nominees = map_nominees_to_awards(cleaned_tweets, awards, List_Awards_Nominee)

    # Map winners to awards
    winners = map_winners_to_awards(cleaned_tweets, awards)

    # Generate output (human-readable format)
    with open('results/output_human_readable.txt', 'w') as file:
        file.write(f"Hosts: {', '.join(hosts)}\n")
        for award in awards:
            file.write(f"Award: {award}\n")
            file.write(f"Presenters: {', '.join(presenters[award])}\n")
            file.write(f"Nominees: {', '.join(nominees[award])}\n")
            file.write(f"Winner: {winners[award]}\n\n")

    # Generate output (JSON format)
    output_json = {
        "Hosts": hosts,
        "Awards": {
            award: {
                "Presenters": presenters[award],
                "Nominees": nominees[award],
                "Winner": winners[award]
            } for award in awards
        }
    }
    with open('results/output.json', 'w') as file:
        json.dump(output_json, file, indent=4)

if __name__ == '__main__':
    main()
