from pyparsing import makeHTMLTags,SkipTo,htmlComment
import re
import urllib2


def alexa():
	url = 'http://www.alexa.com/hoturls'
	r   = '<a class="offsite" href="(.*?)">';
	hotWords = []

	try:
		response = urllib2.urlopen(url)

		
	except urllib2.HTTPError, e:
		print "Error ", e.code, search
		sys.exit()

	lines = response.readlines()

	#pyparse prepare
	aStart,aEnd = makeHTMLTags("A")
	link = aStart + SkipTo(aEnd).setResultsName("link") + aEnd
	link.ignore(htmlComment)

	for line in lines:
		if line.find("title=") != -1:
			for toks,start,end in link.scanString(line):
				hotWords.append(toks.link)

	return hotWords

	
def google_trends():
	trends = []
	user_agent = 'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; en-US)'
	search = "http://www.google.com/trends/hottrends"

	req = urllib2.Request(search) 
	req.add_header('User-Agent', user_agent)

	try:
		response = urllib2.urlopen(req)
	except urllib2.HTTPError, e:
		print "Error ", e.code, search
		sys.exit()

	lines = response.readlines()

	for line in lines:
		if line.find("trends/hottrends") != -1:
			# cut line until trends/hottrends
			line = line[line.find("trends/hottrends"):]
			# trends begin after <
			line = line[line.find(">")+1:]
			# trends ends before >
			trend = line[:line.find("<")]

			if len(trend) > 0 and trend[1] != " " and trend != "Site Feed":
				trends.append(trend)

	return trends


def twitter_trends():

	url = 'http://search.twitter.com/'
	r = "(\/intra\/trend/(.*?)')";
	words = []

	for x, m in enumerate(re.findall(r, urllib2.urlopen(url).read())):
		word = m[1]
		if word[:3] == "%23":
			word = word.replace("%23", "")
			words.append(word)
		else:
			words.append(word)

	return words
		
