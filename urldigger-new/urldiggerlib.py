from BeautifulSoup import BeautifulSoup
from pyparsing import makeHTMLTags,SkipTo,htmlComment
from suspicious_code import *
from xgoogle.search import GoogleSearch, SearchError
import re
import urllib2


class Url:
	
	def __init__(self, host, basepath):

		self.host = host
		self.basepath = basepath


def isJavaScript(url):
	
	p = re.compile('.*javascript:.*')
	m = p.match(url)
	if m:
		return True
	else:
		return False


def openUrl(url):

	try:
		#TODO: debug mode to show this print optional
		print "[OPENING... ] %s"  % url

		opener = urllib2.build_opener()
		#TODO: option to choose USER-AGENT
		opener.addheaders = [('User-Agent', 'Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1; NET CLR 1.1.4322; .NET CLR 2.0.50727; \
							.NET CLR 3.0.4.506.2152 .NET CLR 3.5.30729)')]
		#control url starts with http????
		currentpage = opener.open(url)
		return currentpage

	except Exception, e:
		print "'%s' in url: '%s' at opening"  %(e, url)


def readUrl(currentpage):

	html = currentpage.read()
	currentpage.close()
	return html


def getBaseHref(soup):

	bases = soup.findAll('base')

	for base in bases:
		if base:
			if base.has_key('href'):
				return base['href']


def getLinks(soup):

	hrefs = soup.findAll('a', href=True)
	
	hrefs.extend(soup.findAll('link', href=True))

	links = set()

	for link in hrefs:

		url = link['href']
		links.add(url)
		print "Links: %s\n" %url


def parseHtml(html):

	soup = BeautifulSoup(html)

	links = getLinks(soup)

#By default only level 1
def parseUrl(url):

	links = []

	if isJavaScript(url):
		print "JS: %s" %url
		return links

	try:
		page = openUrl(url)
		
		if page:
			html = readUrl(page)
			contents = parseHtml(html)
			print contents

	except Exception, e:
		print "'%s' in url: '%s'"  %(e, url)


def google(termtosearch, rpp):
	try:
		gs = GoogleSearch(termtosearch)
		#rpp: Results Per Page
		gs.results_per_page = rpp
		results = gs.get_results()
		
		for res in results:
			#print res.url.encode('utf8')
			print "Looking SPAM in %s" %(res.url.encode('utf8'))
			spam_detect(res.url.encode('utf8'))

	except SearchError, e:
		print "Search failed: %s" %e

		

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


def google_trends_urls():
	print "OK"

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


def spam_detect(url):

	spam_url_suspicious = []
	spam_word_suspicious = []
	
	try:
		lines = urllib2.urlopen(url).readlines()
	except:
		pass

	if 'lines' in locals():
		for line in lines:
			for w in SPAM_WORDS:
				if w in line:
					if url not in spam_url_suspicious:
						spam_url_suspicious.append(url)
						spam_word_suspicious.append(w)

	for i in spam_url_suspicious:
		print '\033[1;41mSuspicious SPAM!!!-----> %s ( %s )\033[1;m' %(u, spam_word_suspicious)
