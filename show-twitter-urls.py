#!/usr/bin/env python

import twitter, time
import urlparse
import urllib2
import os

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


api = twitter.Api()


while True:
    #fobj = open('/tmp/manual_uris.txt', 'a')
    statuses = api.GetPublicTimeline()
    for s in statuses:
            if s.user.url != None:
		host = urlparse.urlparse(s.user.url)[1]
		if host != "null":
			print '\033[1;34mLooking for SPAM in........%s (%s)\033[1;m' % (s.user.url,s.user.screen_name )
			spam_detect(s.user.url)
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
