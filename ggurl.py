###################################################################################
#library needed from http://www.catonmat.net/blog/python-library-for-google-search/
#
#Get all urls from a search term in google.
###################################################################################
from xgoogle.search import GoogleSearch, SearchError

try:
  gs = GoogleSearch("christmas")
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
