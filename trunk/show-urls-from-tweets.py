#!/usr/bin/env python

import twitter, time
import urlparse
import urllib2
import os
import sqlite3
from time import strftime
import sys
from time import sleep
import re


api = twitter.Api()

while True:
    statuses = api.GetPublicTimeline()

    for s in statuses:
        if s.user.url != None:
			host = urlparse.urlparse(s.user.url)[1]
			if host != "null":
					#connection = sqlite3.connect('urldigger.db')
					#u = (s.user.url, s.user.screen_name, '0', mitime,)
					#print s.user.screen_name
					statuses2 = api.GetUserTimeline(s.user.screen_name)
					#print [a.text for a in statuses2]
					for a in statuses2:
						urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', a.text)
						if urls:
							print "USER: %s URL: %s" %(s.user.screen_name, urls)
