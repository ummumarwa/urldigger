#!/usr/bin/env python

import twitter, time
import urlparse
import os
#from shorturl import is_short_url, longurl

api = twitter.Api()


while True:
    fobj = open('/tmp/manual_uris.txt', 'a')
    statuses = api.GetPublicTimeline()
    for s in statuses:
            if s.user.url != None:
		host = urlparse.urlparse(s.user.url)[1]
		if host != "null":
            		print "%s" %(s.user.url) 
			fobj.write ('%s\n' %(s.user.url))

			"""
			if is_short_url(s.user.url):
				fobj.write ('%s\n' %longurl(s.user.url))
				print "UNSHORTENED: %s - %s" %(s.user.url,longurl(s.user.url))
			else:
            			print "%s" %(s.user.url) 
				#fobj.write ('%s\n' % s.user.url)
			"""
    fobj.close()
    time.sleep(60)
