#!/usr/bin/env python
# -*- coding: utf8 -*-


"""
Give wplinks a website URL and it will scrape the Wikipedia External link 
search form for 36 Wikipedias and print out the results as tab separated
columns: wikipedia article url, external link url.
"""

import re
import sys
import json
import time
import codecs
import urllib
import urllib2

RETRIES_BETWEEN_ERRORS = 5

def main(website_url):
    langs = ["ar", "bg", "ca", "cs", "da", "de", "el", "en", "eo", "es",
            "eu", "fa", "fi", "fr", "he", "hu", "id", "it", "ja", "ko",
            "lt", "ms", "nl", "no", "pl", "pt", "ro", "ru", "sk", "sl",
            "sv", "tr", "uk", "vi", "vo", "zh"]
    for lang in langs:
        for src, target in links(website_url, lang=lang):
            print src.encode('utf8'), "\t", target.encode('utf8')
    

def links(site, lang='en', page_size=500, offset=0):
    """
    a generator that returns a source, target tuples where source is the
    url for a document at wikipedia and target is a url for a document at 
    a given site
    """
    links_url = 'http://%s.wikipedia.org/w/index.php?title=Special:LinkSearch&target=%s&limit=%s&offset=%s'
    wikipedia_host = 'http://%s.wikipedia.org' % lang
    while True:
        url = links_url % (lang, site, page_size, offset)
        html = codecs.decode(_fetch(url), 'utf8')
        found = 0
        for line in html.split("\n"):
            m = re.search('<li><a class="external".+?href="([^"]+)".+?<a href="(/wiki/[^"]+)"', line)
            if m:
                found += 1
                yield wikipedia_host + m.group(2), m.group(1)  

        if found == page_size:
            offset += page_size
        else:
            break


def _fetch(url, params=None, retries=RETRIES_BETWEEN_ERRORS):
    if params:
        req = urllib2.Request(url, data=urllib.urlencode(params))
        req.add_header('Content-type', 'application/x-www-form-urlencoded; charset=UTF-8')
    else:
        req = urllib2.Request(url)
    req.add_header('User-agent', 'wplinks v0.1')

    try:
        return urllib2.urlopen(req).read()
    except urllib2.URLError, e:
        return _fetch_again(e, url, params, retries)
    except urllib2.HTTPError, e:
        return _fetch_again(e, url, params, retries)


def _fetch_again(e, url, params, retries):
        retries -= 1
        if retries == 0:
            raise e
        else: 
            # should back off 10, 20, 30, 40, 50 seconds
            sleep_seconds = (RETRIES_BETWEEN_ERRORS - retries) * 10
            time.sleep(sleep_seconds)
            return _fetch(url, params, retries)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "usage: wplinks.py <website_url"
        sys.exit(1)
    main(sys.argv[1])
