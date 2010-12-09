#!/usr/bin/env python


# Distributed under MIT license:
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

# 2010 - Emilio Casbas <ecasbas@gmail.com>
#
# Script para verificar si ha habido algun cambio en un dominio.
# Verifica el md5 de la pagina monitorizada, si este no coincide
# con el original, envia un correo avisando de cambios (legitimos o fraudulentos)
# 
# Valido solo para paginas estaticas que no se actualizan, sitios web
# de escaparates, tiendas online, paginas personales, etc.
#

import smtplib
import urllib2
from hashlib import md5
from email.MIMEText import MIMEText


def enviar_correo(url):

	sender = "monitorURL-MD5@server"
	receiver = "micorreo@midominio.com" 

	msg = "From: %s\n" %sender
	msg += "To: %s\n" %receiver
	msg += "Subject: Modificacion en sitio web %s\n\n" %url
        msg += "Revisar si es una modificacion legitima o el sitio ha sido comprometido"

	#Configurado smtp con stunnel
 	server = smtplib.SMTP('localhost:466')
 	server.sendmail(sender, receiver, msg)
 	server.quit()


def check_md5(url):

        #URLS deben ser con http://
        req= urllib2.Request(url)
        response = urllib2.urlopen(req)

        #page contiene todo el html estatico de la pagina
        page = response.read()
        return(md5(page).hexdigest())


def main():
        #Dominios monitorizados, el md5 se saca a mano inicialmente
        dominios = {"emiliocasbas.com":"fb401bc7c3413cc2947b5c066bd589dc",
                   }

        #Meterlo en una lista para monitorizar mas dominios
        emilio = check_md5('http://www.emiliocasbas.com')
        if emilio != dominios["emiliocasbas.com"]:
                print "Dominio Emilio -Algo falla"
                enviar_correo('http://www.emiliocasbas.com')
        else:
                print "Dominio Emilio OK"


if __name__ == "__main__":
        main()
