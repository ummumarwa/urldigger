#!/usr/bin/env python

import twitter, time
import urlparse
import urllib2
import os
import sqlite3
from time import strftime

#from shorturl import is_short_url, longurl
def spam_detect(url):
    fobj = open('/tmp/spam_twitter.txt', 'a')

    spam_words = ['viagra', 'cyalis', 'xenical', 'lipitor',
                  'lexapro', 'zoloft', 'tramadol',
                  'prozac', 'kamagra', 'propecia', 'levitra',
                  'cheap vista for students', 'Generic Pill', 'Secret to increase'
                  'mexican pharmacy phentermine', 'Invia Nasal Viagra'
                  'iframe width="1" height="1"'
                 ]

    spam_url_suspicious = []

    try:
        lines = urllib2.urlopen(url).readlines()
    except:
        #print "URL error %s" %e.reason
        pass

    if 'lines' in locals():
        for line in lines:
            for w in spam_words:
                if w in line:
                    if url not in spam_url_suspicious:
                        spam_url_suspicious.append(url)
    				    #fobj.write ('%s\n' %(url))
  						#fobj.close()

    for u in spam_url_suspicious:
        print '\033[1;41mSuspicious SPAM!!!-----> %s \033[1;m' %(u)


def phishing_detect(url):
        #fill in with all phished sites detected in SPAM folder
        phished_sites_strings = [ 'www.bbva.es',
                                  'www.cajamar.es'
                                ]

        phishing_url_suspicious = []

        try:
                lines = urllib2.urlopen(url).readlines()
        except:
                pass

        if 'lines' in locals():
                for line in lines:
                        for p in phished_sites_strings:
                                if p in line and p not in url:
                                        if url not in phishing_url_suspicious:
                                                phishing_url_suspicious.append(url)

        for u in phishing_url_suspicious:
            print '\033[1;41mSuspicious PHISHING!!!-----> %s\033[1;m' %u

api = twitter.Api()


while True:
    #fobj = open('/tmp/manual_uris.txt', 'a')
    statuses = api.GetPublicTimeline()
    #//connection = sqlite3.connect('urldigger.db')
    #cursor = connection.cursor()
    #mitime = strftime("%Y-%m-%d %H:%M:%S")
	#connection = sqlite3.connect('urldigger.db')
    for s in statuses:
            if s.user.url != None:
		host = urlparse.urlparse(s.user.url)[1]
		if host != "null":
			connection = sqlite3.connect('urldigger-pruebas')
			cursor = connection.cursor()
			mitime = strftime("%Y-%m-%d %H:%M:%S")
			cursor.execute("INSERT INTO urls(url, user, result, timescan) values('%s', '%s', 0, '%s')" % (s.user.url, s.user.screen_name, mitime))
			connection.commit()
			connection.close()
			print '\033[1;34mLooking for SPAM in........%s (%s)\033[1;m' % (s.user.url,s.user.screen_name )
			spam_detect(s.user.url)
			print '\033[1;34mLooking for PHISHING in........%s (%s)\033[1;m' % (s.user.url,s.user.screen_name )
			phishing_detect(s.user.url)
		    #fobj.write ('%s\n' %(s.user.url))

			"""
			if is_short_url(s.user.url):
				fobj.write ('%s\n' %longurl(s.user.url))
				print "UNSHORTENED: %s - %s" %(s.user.url,longurl(s.user.url))
			else:
            			print "%s" %(s.user.url) 
				#fobj.write ('%s\n' % s.user.url)
			"""
    #fobj.close()
    time.sleep(30)
