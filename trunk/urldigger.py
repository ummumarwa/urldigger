#!/usr/bin/python

from optparse import OptionParser

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


def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-g", "--goog", dest="term",
                      help="get urls with search term=term from google. Default is 100")
    parser.add_option("-u", "--ul", dest="ulimit",
                      help="no limit in the number of search url gets from google. Default is 100")
    parser.add_option("-a", "--alexa", dest="country",
                      help="get urls from alexa top sites with country=ES,EN ")
    parser.add_option("-f", "--file", dest="filename",
                      help="read data from FILENAME")
    parser.add_option("-v", "--verbose",
                      action="store_true", dest="verbose")
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose")
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
		print "ES"
	elif options.country == 'EN':
		print "EN"
	else: print 'country option: \'%s\' not valid' %options.country

    if options.term:
	termtosearch = options.term
	googledefault(termtosearch)

if __name__ == "__main__":
    main()

