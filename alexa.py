# -*- coding: utf-8 -*-
import os

#extrae 300 topsites + 20 hoturls
alexa = "http://www.alexa.com/hoturls"
comando = "hrefs.sh " + alexa
os.system(comando + '|grep -v alexa')

url ="\"http://www.alexa.com/topsites/global;\""
n = 1
while n < 25:
	top100 = url + repr(n)
	comando = "hrefs.sh " + top100
	os.system(comando + '|grep -v alexa') 
	n+=1

#TOP SITES POR PAIS
alexa = "http://www.alexa.com/topsites/countries/ES"
comando = "hrefs.sh " + alexa
os.system(comando + '|grep -v alexa')

url ="\"http://www.alexa.com/topsites/countries;\""
n = 1
while n < 25:
	topES = url + repr(n) + "/ES"
	comando = "hrefs.sh " + topES
	os.system(comando + '|grep -v alexa') 
	n+=1
