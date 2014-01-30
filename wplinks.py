import re
import json
import urllib
import urlparse

def extlinks(url, lang="en"):
    """
    a generator that returns source, target tuples where source is the
    url for a document at wikipedia and target is a url for a document at
    a given site.
    """
    api_url = "https://%s.wikipedia.org/w/api.php?action=query&list=exturlusage&euquery=%s&eulimit=500&format=json&euoffset=%i"

    u = urlparse.urlparse(url)
    query = u.netloc + u.path

    offset = 0
    while True:
        results = _get_json(api_url % (lang, query, offset))
        for link in results['query']['exturlusage']:
            title = urllib.quote(link['title'].replace(' ', '_').encode('utf8'))
            wp_url = 'https://%s.wikipedia.org/wiki/%s' % (lang, title)
            yield (wp_url, link['url'])
        if 'query-continue' in results:
            offset = results['query-continue']['exturlusage']['euoffset']
        else:
            break


def links(article_url):
    """
    Pass links a URL for a Wikipedia article and you will get a generator 
    for Wikipedia URLs that are linked to from that page.
    """
    m = re.match('http(?s)?://(..).wikipedia.org/wiki/(.+)$', article_url) 
    if not m:
        raise Exception("invalid Wikipedia URL: %s" % article_url)
    lang = m.group(1)
    title = m.group(2)
    url = 'https://%s.wikipedia.org/w/api.php?action=query&prop=links&titles=%s&pllimit=500&format=json' % (lang, title)

    cont = None
    while True:
        if cont:
            u = url + '&plcontinue=' + urllib.quote(cont.encode('utf-8'))
        else:
            u = url
        results = _get_json(u)
        page_id = results['query']['pages'].keys()[0]
        if page_id != -1:
            for link in results['query']['pages'][page_id]['links']:
                yield 'https://%s.wikipedia.org/wiki/%s' % \
                        (lang, _escape(link['title']))
            if 'query-continue' in results:
                cont = results['query-continue']['links']['plcontinue']
            else:
                break


def _escape(s):
    return urllib.quote(s.encode('utf8').replace(' ', '_'))


def _get_json(url):
    resp = urllib.urlopen(url)
    results = json.loads(resp.read())
    return results
