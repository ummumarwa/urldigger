#!/usr/bin/python

import os
#from optparse import OptionParser
import optparse

# (check this library on run time)
from xgoogle.search import GoogleSearch, SearchError

# by default only print 100 first results
def googledefault(termtosearch):
	try:
	  gs = GoogleSearch(termtosearch)
	  gs.results_per_page = 50
	  results = gs.get_results()
	  for res in results:
	    print res.url.encode('utf8')
	except SearchError, e:
	  print "Search failed: %s" % e

def google(termtosearch):
	try:
	  gs = GoogleSearch(termtosearch)
	  gs.results_per_page = 100
	  results = []
	  while True:
	    tmp = gs.get_results()
	    if not tmp:
	      break
	    results.extend(tmp)
	  for res in results:
	    print res.url.encode('utf8')
	except SearchError, e:
	  print "Search failed: %s" % e	

def alexa(country, n):
	if country == "ES":
		alexaES("ES")
	elif country == "EN":
		if n >= 1:
			# max 24 number = 2400 results. To-check
			num = calculateN(n)
			alexaEN(num)
		else: alexaEN(2)


def calculateN(n):
	if n == 20:
		return(2)
	elif n == 40:
		return(3)
	elif n == 60:
		return(4)
	elif n == 80:
		return(5)
	elif n == 100:
		return(6)
	elif n == 120:
		return(7)
	elif n == 140:
		return(8)
	elif n == 160:
		return(9)
	elif n == 180:
		return(10)
	elif n == 200:
		return(11)
	
	# Default return 2 -> 20 results
	else: return(2)

def alexaES(country):
	alexa = "http://www.alexa.com/topsites/countries/ES"
	# check if hrefs.sh script exists
	comando = "./hrefs.sh " + alexa
	os.system(comando + '|grep -v alexa')

def alexaEN(num):
	url ="\"http://www.alexa.com/topsites/global;\""
	# n=2 -> 20 results
	n = 1
	while (n < num):
		top100 = url + repr(n)
		comando = "./hrefs.sh " + top100
		os.system(comando + '|grep -v alexa') 
		n+=1

def alexaHOT():
	alexa = "http://www.alexa.com/hoturls"
	comando = "./hrefs.sh " + alexa
	os.system(comando + '|grep -v alexa')

	
def main():
    usage = "usage: %prog [options] arg"
    parser = optparse.OptionParser(usage)

    # Commands
    commands = optparse.OptionGroup(parser, "Commands")
    commands.add_option("-H", "--hot", action="store_true",
			help="get hot urls from alexa. [default 20]")
    commands.add_option("-u", "--ulimit", action="store_true",
                      help="no limit in the number of search url gets from google with '-g option'")
    parser.add_option_group(commands)


    # Options
    options = optparse.OptionGroup(parser, "Options")
    options.add_option("-a", "--alexa", dest="country", 
			help="get urls from alexa top sites with selected country (EN, ES). [default 20]")
    options.add_option("-g", "--goog", dest="term",
                      help="get urls with search term=term from google [default 50]")
    options.add_option("-n", "--num", dest="number", type="int",
                      help="specify number urls to get with 'option -a' (20,40,60,80,100,120). [default 20]")
    parser.add_option_group(options)
    

    # Output
    output = optparse.OptionGroup(parser, "Output")
    output.add_option("-v", "--verbose",
                      action="store_true", dest="verbose")
    output.add_option("-q", "--quiet",
                      action="store_false", dest="verbose")
    parser.add_option_group(output)

    (options, args) = parser.parse_args()

    if len(args) == 1:
	print "URL digger services (extract urls from websites)"
	print "by user (mail at user)"
	print
        parser.error("incorrect number of arguments")

    if options.verbose:
        print "reading %s..." % options.filename

    if options.country:
	if options.country == 'ES':
		alexa("ES", 1)
	elif options.country == 'EN':
		if options.number:
			alexa("EN", options.number)
		else: alexa("EN", 1)
	else: print 'country option: \'%s\' not valid' %options.country

    if options.hot:
	alexaHOT()

    #if options.number:
#	print "Number specified"

    if options.term:
	if options.ulimit:
		google(options.term)
	else: googledefault(options.term)

if __name__ == "__main__":
    main()

