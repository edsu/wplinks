wplinks
=======

[![Build Status](https://secure.travis-ci.org/edsu/wplinks.png)](http://travis-ci.org/edsu/wplinks)

wplinks provides a the `links` function that returns a generator for links 
from Wikipedia articles to a particular website, or portion of a website. It 
actually just iteratively scrapes the results of the 
[External links search][1] page.

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
