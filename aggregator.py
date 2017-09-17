from scraper import *
import string

class Aggregator(ScraperDelegate):
    scraper = None
    scrapedTweets = []
    def __init__(self):
        self.scraper = Scraper(self)

    def aggregate(self, twitterHandle):
        return self.scraper.scrape(twitterHandle)

    def scraped(self, tweets):
        self.scrapedTweets = tweets

def removePunc(inputString):
    for char in inputString: 
        if char in string.punctuation:
            inputString.remove(char)
    return inputString

class dataSet():
    def __init__(self, twitterHandle):
        self.tweetSet = dict()
        self.speechSet = dict()
        ag = Aggregator()
        self.tweets = ag.aggregate(twitterHandle)
        self.speeches = []
    def populate(self):
        for tweet in self.tweets:
            words = tweet.strip().split()
            for word in words:
                if word.lower().startswith("https:"):
                    continue 
                word = word.translate({ord(i):None for i in string.punctuation}).lower()
                if word in self.set:
                    self.tweetSet[word] += 1
                else:
                    self.tweetSet[word] = 1
        for datum in self.tweetSet:
            print datum, self.tweetSet[datum]


        for speech in speeches:
            words = speech.strip().split()
            for word in words:
                if word.lower().startswith("https:"):
                    continue 
                word = word.translate({ord(i):None for i in string.punctuation}).lower()
                if word in self.set:
                    self.speechSet[word] += 1
                else:
                    self.speechSet[word] = 1
        for datum in self.speechSet:
            print datum, self.speechSet[datum]
