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


def spam_detect(url):
    connection = sqlite3.connect('twitturls.db')
    cursor = connection.cursor()

    spam_words = ['buy viagra', 'buy cyalis', 'buy xenical', 'buy lipitor',
                                  'generic viagra', 'viagra online',
                                  'comprar viagra', 'comprar cyalis', 'comprar propecia',
                  'buy exapro', 'buy oloft', 'buy tramadol',
                  'buy prozac', 'buy kamagra', 'buy propecia', 'buy levitra',
                  'cheap vista for students', 'Generic Pill', 'Secret to increase'
                  'mexican pharmacy phentermine', 'Invia Nasal Viagra'
                  'iframe width="1" height="1"'
                 ]

    spam_url_suspicious = []
    spam_word_suspicious = []

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
                        spam_word_suspicious.append(w)
                        u = (w, url,)
                        cursor.execute("UPDATE urls set result = 1, suspicious_word = ?  WHERE url=?", u)
                        connection.commit()
                        connection.close()


    for u in spam_url_suspicious:
        print '\033[1;41mSuspicious SPAM!!!-----> %s ( %s ) \033[1;m' %(u, spam_word_suspicious)


def phishing_detect(url):
        #fill in with all phished sites detected in SPAM folder
        phished_sites_strings = [ 'www.bbva.es', 'www.cajamar.es', 'www.bancopopular.es', 'www.bbva.es', 'www.bancopastor.es'
                                  'www.caixasabadell.es', 'www.cajacantabria.com', 'www.cajamadrid.es', 'www.bancasabadell.es'
                                  'www.bancaja.es', 'www.bancomercio.com', 'www.bde.es', 'www.bancogui.es', 'www.bancopastor.es'
                                  'www.bancopopular.es', 'www.banesto.es', 'www.bankinter.es', 'www.caixacat.es' 
                                ]

        phishing_url_suspicious = []
        phishing_site_suspicious = []

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
                                                phishing_site_suspicious.append(p)

        for u in phishing_url_suspicious:
            print '\033[1;41mSuspicious PHISHING!!!-----> %s ( %s )\033[1;m' %(u, phishing_site_suspicious[0])


#body code
api = twitter.Api()

while True:
    statuses = api.GetPublicTimeline()

    for s in statuses:
		users = api.GetUserTimeline(s.user.screen_name)
		for a in users:
			urls = re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', a.text)
			if urls:
				myUrl = (urls.group(),)
				connection = sqlite3.connect('twitturls.db')
				cursor = connection.cursor()
				cursor.execute("SELECT url FROM urls WHERE url = ?", myUrl)
				connection.commit()
				data = cursor.fetchone()
				if data is None:
					mitime = strftime("%Y-%m-%d %H:%M:%S")
					data_collected = (urls.group(), a.user.screen_name,mitime,)
					print '\033[1;34mLooking for SPAM in........%s (%s)\033[1;m' % (myUrl, a.user.screen_name )
					spam_detect(myUrl)
					cursor.execute("INSERT INTO urls(url, user, timescan) values(?, ?, ?)", data_collected)
					connection.commit()
					connection.close()
