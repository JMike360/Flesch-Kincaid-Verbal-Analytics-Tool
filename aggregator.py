from scraper import *
import string

class Aggregator(ScraperDelegate):
    scraper = None

    def __init__(self):
        self.scraper = Scraper(self)

    def aggregate(self):
        return self.scraper.scrape()

    def scraped(self, tweets):
        print "scraped tweets:"

        i = 1

        for t in tweets:
            print ("%d. " % i) + t + "\n"
            i += 1

def removePunc(inputString):
    for char in inputString:
        if char in string.punctuation:
            inputString.remove(char)
    return inputString

class dataSet():
    def __init__(self):
        self.tweetSet = dict()
        self.speechSet = dict()
        ag = Aggregator()
        self.tweets = ag.aggregate()
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
d = dataSet()
d.populate()