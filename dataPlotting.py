from aggregator import *
from flesch import *
import matplotlib.pyplot as plt
def getDonaldTrumpTweetsFromAPI():
	ag = Aggregator()
	ag.aggregate('@realDonaldTrump')
	return ag.scrapedTweets
def getDonaldTrumpFleschScoresFromFile():
	fleschTest = Flesch()
	return fleschTest.test('drumpf.json')
class dateTime():
	time = 0
	month = 0
	day = 0
	year = 0
	def parseDateTimeFromTwitterString(self, string):
		obj = dateTime()
		months = { 	'Jan' : 1,
					'Feb' : 2,
					'Mar' : 3,
					'Apr' : 4,
					'May' : 5,
					'Jun' : 6,
					'Jul' : 7,
					'Aug' : 8,
					'Sep' : 9,
					'Oct' : 10,
					'Nov' : 11,
					'Dec' : 12
				  }
		obj.month = int(months[string[4:7]])
		obj.day = int(string[8:10])
		obj.time = int(string[11:13])*3600 + int(string[14:16])*60 + int(string[17:19])
		obj.year = int(string[-4:])
		return obj
	def compare(self, DateTime):
		return self.getPlottingValue() - DateTime.getPlottingValue()
	def getPlottingValue(self):
		secondsToDays = self.time/(3600.0 * 24.0)

		monthDays = {1 : 31,
					 2 : 28,
					 3 : 31,
					 4 : 30,
					 5 : 31,
					 6 : 30,
					 7 : 31,
					 8 : 31,
					 9 : 30,
					 10: 31,
					 11: 30,
					 12: 31}

		daysToMonths = float(secondsToDays + self.day) / float(monthDays[self.month])
		return self.year + (float(self.month + daysToMonths)/12.0)

xplot = []
yplot = []
results = getDonaldTrumpFleschScoresFromFile()
for result in results:	
	d = dateTime()
	parsed = d.parseDateTimeFromTwitterString(result[1]['created_at'])
	time = parsed.getPlottingValue()

	xplot.append(time)
	yplot.append(result[0])
print xplot
plt.plot(xplot, yplot, 'r+')
plt.show()