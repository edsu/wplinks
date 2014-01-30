from wplinks import extlinks, links
from urlparse import urlparse


def test_extlinks():
    results = list(extlinks("http://www.theparisreview.org/interviews"))
    assert len(results) > 0
    assert len(results[0]) == 2
    u = urlparse(results[0][0])
    assert u.netloc == 'en.wikipedia.org'
    u = urlparse(results[0][1])
    assert u.netloc == 'www.theparisreview.org'
    assert u.path.startswith('/interviews')

def test_extlinks_lang():
    results = list(extlinks("http://www.theparisreview.org/interviews", lang='fr'))
    assert len(results) > 0
    u = urlparse(results[0][0])
    assert u.netloc == 'fr.wikipedia.org'
    u = urlparse(results[0][1])
    assert u.netloc == 'www.theparisreview.org'
    assert u.path.startswith('/interviews')

def test_extlinks_paging():
    results = list(extlinks("http://www.theparisreview.org"))
    assert len(results) > 500

def test_links():
    results = list(links("http://en.wikipedia.org/wiki/Philosophy"))
    assert len(results) > 500
    assert results[0].startswith('https://en.wikipedia.org/wiki/')
