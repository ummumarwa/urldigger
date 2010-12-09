#!/usr/bin/env python

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
