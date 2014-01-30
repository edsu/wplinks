import json
import urllib
import urlparse

def links(url, lang="en"):
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
        resp = urllib.urlopen(api_url % (lang, query, offset))
        results = json.loads(resp.read())
        for link in results['query']['exturlusage']:
            title = urllib.quote(link['title'].replace(' ', '_').encode('utf8'))
            wp_url = 'http://%s.wikipedia.org/wiki/%s' % (lang, title)
            yield (wp_url, link['url'])
        if 'query-continue' in results:
            offset = results['query-continue']['exturlusage']['euoffset']
        else:
            break
