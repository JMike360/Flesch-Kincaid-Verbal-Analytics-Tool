import twitter

class ScraperDelegate:
    def scraped(self, tweets):
        pass

class Scraper:
    url = ''
    delegate = None
    api = twitter.Api(consumer_key='Zo10vna6EddbVXPKlA8NOB5Fw',
                      consumer_secret='pVGFprF5B6lYv03Om7jsaOFrZmNc2XMYixbzUiEiiaFzrwUBAZ',
                      access_token_key='2355912032-hwIgcQaArMtdFYGsKB44ET828JJ1GGKn9pH0zFK',
                      access_token_secret='V3gWjk8JoebKg7iMLoV0nEfMsvO5nQXNJD8zTRen7YJ5i')

    def __init__(self, delegate):
        if isinstance(delegate, ScraperDelegate):
            self.delegate = delegate

    def scrape(self, twitterHandle):
        statuses = self.api.GetUserTimeline(screen_name=twitterHandle) #'@realDonaldTrump'

        for s in statuses:
            print s

        ret = []

        for s in statuses:
            ret.append(s.text)

        self.delegate.scraped(ret)
