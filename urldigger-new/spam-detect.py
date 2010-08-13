#!/usr/bin/env python

################################################################
#
# POC to detect spam incrusted in sites and suspicious javascript
#
# TODO: crawl each site
#       more spam words detection
#       more suspicious javascript detection 
#       programming exceptions opening urls 
#
################################################################

from datetime import date
import re
import urllib2


now = date.today()
FECHA= now.strftime("%Y%m%d")

spam_words = ['viagra', 'cyalis', 'xenical', 'lipitor',
              'soma', 'lexapro', 'zoloft', 'tramadol',
              'prozac', 'kamagra', 'propecia', 'levitra',
             ]

javascript_suspicious = ['eval(', '$="']

spam_url_suspicious = []
javascript_url_suspicious = []

#print "%s" %FECHA

#url = "http://put-here-tu-url-to-test"
#or instead use a file with plenty of urls maybe extracted with urldigger ;)
#http://code.google.com/p/urldigger/

f = open('universidades.txt', 'r')
allLines = f.readlines()
f.close()

for url in allLines:
	lines = urllib2.urlopen(url).readlines()
	for line in lines:
		for w in spam_words:
			if w in line:
				if url not in spam_url_suspicious:
					spam_url_suspicious.append(url)
		for w in javascript_suspicious:
			if w in line:
				if url not in javascript_url_suspicious:
					javascript_url_suspicious.append(url) 
			

for u in spam_url_suspicious:
	print "Suspicious SPAM --> %s" %u

for u in javascript_url_suspicious:
	print "Suspicious JAVASCRIPT --> %s" %u


