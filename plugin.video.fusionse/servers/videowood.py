# -*- coding: iso-8859-1 -*-
# ------------------------------------------------------------
# fusionse - XBMC Plugin
# Conector for videowood.tv
# http://www.mimediacenter.info/foro/viewforum.php?f=36
# by DrZ3r0
# ------------------------------------------------------------

import re
from core import logger
from core import scrapertools


def test_video_exists(page_url):
    logger.info("fusionse.servers.videowood test_video_exists(page_url='%s')" % page_url)

    data = scrapertools.cache_page(page_url)

    if "This video doesn't exist." in data:
        return False, 'The requested video was not found.'

    return True, ""


def get_video_url(page_url, premium=False, user="", password="", video_password=""):
    logger.info("fusionse.servers.videowood url=" + page_url)
    video_urls = []

    data = scrapertools.cache_page(page_url)
    text_encode = scrapertools.find_single_match(data, "(eval\(function\(p,a,c,k,e,d.*?)</script>")

    from aadecode import decode as aadecode
    text_decode = aadecode(text_encode)

    # URL del v�deo
    patron = "'([^']+)'"
    media_url = scrapertools.find_single_match(text_decode, patron)

    video_urls.append([media_url[-4:] + " [Videowood]", media_url])

    return video_urls


# Encuentra v�deos del servidor en el texto pasado
def find_videos(data):
    encontrados = set()
    devuelve = []

    patronvideos = r"https?://(?:www.)?videowood.tv/(?:embed/|video/)[0-9a-z]+"
    logger.info("fusionse.servers.videowood find_videos #" + patronvideos + "#")

    matches = re.compile(patronvideos, re.DOTALL).findall(data)

    for url in matches:
        titulo = "[Videowood]"
        url = url.replace('/video/', '/embed/')
        if url not in encontrados:
            logger.info("  url=" + url)
            devuelve.append([titulo, url, 'videowood'])
            encontrados.add(url)
        else:
            logger.info("  url duplicada=" + url)

    return devuelve
