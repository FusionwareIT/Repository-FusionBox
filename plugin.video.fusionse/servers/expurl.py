# -*- coding: utf-8 -*-
#------------------------------------------------------------
# fusionse - XBMC Plugin
# Conector para longurl (acortador de url)
# http://www.mimediacenter.info/foro/viewforum.php?f=36
#------------------------------------------------------------


import urlparse

from lib import unshortenit

SERVICES_SHORT = ["adf.ly","sh.st","bit.ly","ul.to"]

def expand_url(url):
    
    e = unshortenit.UnshortenIt()
    
    while Es_Corto(url):
        long_url,estado = e.unshorten(url)
        url = long_url 
                       
    return long_url    
        
def Es_Corto(url):
    
    server = urlparse.urlsplit(url).netloc
    Corto = (server in SERVICES_SHORT)
    return Corto        