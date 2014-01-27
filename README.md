wplinks
=======

wplinks is a simplistic little function for getting a list of links from
Wikipedia articles to a particular website, or portion of a website. It 
actually just scrapes the results of the [External links search][1] page.

Usage
-----

```python

import wplinks

for src, target in links('http://www.theparisreview.org/interviews'):
    print src, target
```

License
-------

* CC0

[1]: https://en.wikipedia.org/wiki/Special:LinkSearch
