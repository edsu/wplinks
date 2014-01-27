from wplinks import links
from urlparse import urlparse


def test_links():
    results = list(links("http://www.theparisreview.org/interviews"))
    assert len(results) > 0
    assert len(results[0]) == 2
    u = urlparse(results[0][0])
    assert u.netloc == 'en.wikipedia.org'
    u = urlparse(results[0][1])
    assert u.netloc == 'www.theparisreview.org'
    assert u.path.startswith('/interviews')


