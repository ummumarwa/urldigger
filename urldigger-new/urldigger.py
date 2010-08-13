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


import optparse
import os
#import re
import threading
from urldiggerlib import *
from time import sleep, ctime
#Thanks to Peteris Krumins for give permission and authored this great library
from xgoogle.search import GoogleSearch, SearchError

version = "03c"

def main():
	usage = "Usage: %prog [options] -h to show HELP" 
	parser = optparse.OptionParser(usage)

	# Commands
	commands = optparse.OptionGroup(parser, "Commands")
	commands.add_option("-a", "--alexa", action="store_true", #dest="alexa", #default="Defecto", action="store_true",
		help="show hot urls from alexa")
	commands.add_option("-g", "--goog", action="store_true",
		help="show google trends")
	commands.add_option("-t", "--twitrends", action="store_true",
		help="show twitter trends")

	parser.add_option_group(commands)

	(options, args) = parser.parse_args()
	if len(args) == 1 or len(args) == 0:
		print "URLDIGGER (extract urls from hot sources and websites)"
		print "by ecasbas (ecasbas at gmail.com)"
		print ""

	# Option choosed
	#----------------------------------------------------------------------------------------------
	if options.alexa:
		a_alexa = alexa()
		print a_alexa

	if options.goog:
		g_trends = google_trends()
		print g_trends

	if options.twitrends:
		t_trends = twitter_trends()
		print t_trends
	

############### MAIN PROGRAM ###########################
if __name__ == "__main__":
	main()
