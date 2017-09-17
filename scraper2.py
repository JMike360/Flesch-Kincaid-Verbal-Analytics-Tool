import json

class Scraper2:
    def scrape(self):
        tweets = json.load(file('drumpf.json'))

        ret = []

        for tweet in tweets:
            text = tweet['text']
            ret += text

        return ret