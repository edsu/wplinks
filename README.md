wplinks
=======

[![Build Status](https://secure.travis-ci.org/edsu/wplinks.png)](http://travis-ci.org/edsu/wplinks)

wplinks provides a generator function called `extlinks` that lets you iterate
through links from Wikipedia articles to a particular website, or portion 
of a website. It also provides `links` which lets you iterate through other
Wikipedia URLs that are linked from a given Wikipedia URL.

So for example, to see what Wikipedia articles point at interviews on the
The Paris Review website:

```python

from wplinks import extlinks 

for src, target in extlinks('http://www.theparisreview.org/interviews'):
    print src, target
```

By default you get links for English Wikipedia, but if you'd like results for 
the French Wikipedia instead use the `lang` parameter:

```python
from wplinks import extlinks

for src, target in extlinks('http://www.theparisreview.org/interviews', lang='fr'):
    print src, target
```

If you'd like to see what other Wikipedia articles a given Wikipedia article
links to use the `links` function. For example lets say you want to see what
articles the James Joyce article points to:

```

from wplinks import links

for url in links('http://en.wikipedia.org/wiki/James_Joyce'):
    print url
```

Why?
----

wplinks used to be somewhat involved since it scraped the 
[External links search][1] page. It became quite a bit simpler once I 
discovered the `exturlusage` [API][2] call. You might want to make this 
API call yourself and page through the results, without including wplinks
as a dependency.  But I left it here just in case you'd rather not.


License
-------

* CC0

[1]: https://en.wikipedia.org/wiki/Special:LinkSearch
[2]: https://en.wikipedia.org/w/api.php
