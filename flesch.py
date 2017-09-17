## Flesch readability test

import json
from operator import itemgetter

import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict
d = cmudict.dict()

def nsyl(word):
    try:
        data = d[word.lower()]
        if len(data) > 0:
            pronunciation = data[0]
            count = 0
            for group in pronunciation:
                if group[-1].isdigit():
                    count += 1
            return count
        else:
            return 0

    except Exception, e:
        pass

    return 0

class Flesch:
    def __init__(self):
        pass

    def flesch_test(self, words, syllables, sentences):
        return (0.39 * (words / sentences)) + (11.8 * (syllables / words)) - 15.59

    def test(self, fileName):
        tweets = json.load(file(fileName)) #drumpf.json

        results = []

        for tweet in tweets:
            tweetSyllables = 0
            text = tweet['text']
            for word in text.split(' '):
                # print "testing word %s" % word
                wordSyllables = nsyl(word)
                tweetSyllables += wordSyllables

            results.append( ([ self.flesch_test(len(text.split(' ')), tweetSyllables, 1)], tweet) )
            #results.append(tweet)
        #results = sorted(results, key=itemgetter(0))
        return results
        #count = 0
        #for result in results:
        #    print result
        #    count += 1
        #
        #print count
            
        # breakeze
    def test_speech(self, fileName):
        with open(fileName, "r") as f:
            single_data_point = 0
            lines = f.read().split('.')
            scores = []
            for line in lines:
                # print line

                sentence_count = max(1, line.count('.') + line.count('!') + line.count('?'))
                words = line.split(' ')
                word_count = len(words)
                syllables_count = 0
                for word in words:
                    syllables_count += nsyl(word)

                line_grade = self.flesch_test(word_count, syllables_count, sentence_count)
                single_data_point += line_grade
                #print("%d" % line_grade)
                scores.append(line_grade)
            single_data_point /= len(lines)
            #print("average: %d" % single_data_point)
        return (scores, single_data_point)
#f = Flesch()
#f.test_speech("drumpf.json")


