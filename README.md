wplinks
=======

[![Build Status](https://secure.travis-ci.org/edsu/wplinks.png)](http://travis-ci.org/edsu/wplinks)

wplinks provides a generator function called `links` that lets you iterate
through links from Wikipedia articles to a particular website, or portion 
of a website. 

wplinks used to be somewhat involved since it scraped the 
[External links search][1] page. It became quite a bit simpler once I 
discovered the `exturlusage` [API][2] call. You might want to make this 
API call yourself and page through the results, without including wplinks
as a dependency.  But I left it here just in case you'd rather not.

Usage
-----

```python

from wplinks import links 

for src, target in links('http://www.theparisreview.org/interviews'):
    print src, target
```

If you'd like results for a non English wikipedia use the lang parameter:

```python

for src, target in links('http://www.theparisreview.org/interviews', lang='fr'):
    print src, target
```

License
-------

* CC0

[1]: https://en.wikipedia.org/wiki/Special:LinkSearch
[2]: https://en.wikipedia.org/w/api.php
