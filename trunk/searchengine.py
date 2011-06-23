
import urllib2
from BeautifulSoup import *
from urlparse import urljoin		

#Lista de palabras a ignorar
ignorewords=set(['the', 'of', 'to',
				'and', 'a', 'in',
				'is', 'it',
				])


class crawler:
	#Inicializa el crawler con nombre de la BBDD
	def __init__(self,dbnmae):
		pass

	def __del__(self):
		pass

	def dbcommit(self):
		pass

	#Funcion auxiliar para obtener un id de entrada y anadirlo si no esta
	def getentryid(self, table, field, value, createnew=True):
		return None

	#Indice de una pagina individual
	def addtoindex(self, url, soup):
		print 'Indexing %s' %url

	#Extrae el texto de la pag HTML (no tags)
	def gettextonly(self, soup):
		return None

	#Separa las palabras por cualquier caracter que no sea espacio
	def separatewords(self, text):
		return None


	#Devuelve verdadero si la URL ya esta indexada
	def isindexed(self, url):
		return False

	#Anade un enlace entre las dos paginas
	def addlinkref(self, urlFrom, urlTo, linkText):
		pass

	#Empieza con una lista de paginas, mira la profundidad dada, y va indexando
	def crawl(self, pages, depth=2):
		pass

	#Crea las tablas de la BBDD
	def createindextables(self):
		pass
	
	def crawl(self, pages, depth=2):
		for i in range(depth):
			newpages=set()
			for page in pages:
				try:
					c = urllib2.urlopen(page)
				except:
					print 'Could not open %s' %page
					continue
				soup=BeautifulSoup(c.read())
				self.addtoindex(page, soup)

				links=soup('a')
				for link in links:
					if ('href' in dict(link.attrs)):
						url = urljoin(page,link['href'])
						if url.find("'") != -1: continue
						url = url.split('#')[0] #borra la parte location
						if url[0:4]=='http' and not self.isindexed(url):
							newpages.add(url)
						linkText=self.gettextonly(link)
						self.addlinkref(page, url, linkText)

				self.dbcommit()

			pages=newpages
