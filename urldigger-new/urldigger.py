#!/usr/bin/python

# Distributed under MIT license:
#
# Copyright (c) 2010 Emilio Casbas (ecasbas at gmail dot com)


# CONTRIBUTORS
# Clemens Kurtenbach

#
# Permission is hereby granted, free of charge, to any person
# Obtaining a copy of this software and associated documentation
# Files (the "Software"), to deal in the Software without
# Restriction, including without limitation the rights to use,
# Copy, modify, merge, publish, distribute, sublicense, and/or sell
# Copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# Conditions:
#
# The above copyright notice and this permission notice shall be
# Included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# TODO:FIXME
#
# Feedback and improvements are welcome! :-)

#deprecated now using argparse
#import optparse
import argparse
import os
import threading
from urldiggerlib import *
from time import sleep, ctime
#Thanks to Peteris Krumins for give permission and authored this great library
from xgoogle.search import GoogleSearch, SearchError

version = "1b"

def main():
	parser = argparse.ArgumentParser(description='urldigger tool to extract HOT topics and urls associated.')

	parser.add_argument('-v', '--version', action='version', version='%(prog)s 1b')
	parser.add_argument('-a', '--alexa', action='store_true', help='show alexa hot words')
	parser.add_argument('-g', '--goog', action='store_true', help='show google trends')
	parser.add_argument('-G', '--googtrendsurls', action='store_true', help='show google trends urls')
	parser.add_argument('-s', '--googsearch', action='store', dest='googsearch', help='show urls from a google search')
	parser.add_argument('-t', '--twitrends', action='store_true', help='show twitter trends')
	parser.add_argument('-T', '--twitrendsurls', action='store_true', help='show twitter trends urls')

	args = parser.parse_args()

	print "URLDIGGER (extract urls from hot sources and websites)"
	print "by Emilio Casbas (ecasbas at gmail.com)"
	print ""

	# Option choosed
	#----------------------------------------------------------------------------------------------
	if args.alexa:
		a_alexa = alexa()
		print a_alexa

	if args.goog:
		g_trends = google_trends()
		print g_trends

	if args.googtrendsurls:
		g_trends = google_trends()
		for i in g_trends:
			google(i, 20)

	if args.googsearch:
		google(args.googsearch, 20)

	if args.twitrends:
		t_trends = twitter_trends()
		print t_trends

	if args.twitrendsurls:
		t_trends = twitter_trends()
		for i in t_trends:
			google(i, 20)
	

############### MAIN PROGRAM ###########################
if __name__ == "__main__":
	main()
