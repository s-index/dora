# dora

## input

```
poetry run dora search 'Python.*' https://www.python.org/blogs/ | jq .
```

## output

```
[
  {
    "title": "Our Blogs | Python.org",
    "url": "https://www.python.org/blogs/",
    "found_search_words": [
      "Python 3.9.0rc1 is now available",
      "Python Events",
      "Python 3.5.10rc1 is now available",
      "Python Insider via:",
      "Python-Dev mailing list",
      "Python Brochure",
      "Python Conferences",
      "Python Events Archive",
      "Python Network",
      "Python",
      "Python 3.5.10 is now available",
      "Python.org",
      "Python Insider",
      "Python Essays",
      "Python 3.7.9 and 3.6.12 security updates now available",
      "Python Wiki",
      "Python 3.5.10 is now available.  You can get it here.",
      "Python Software Foundation",
      "Python Books",
      "Python Software Foundation End-of-the-Year Fundraiser",
      "Python Insider by the Python Core Developers is licensed under a ",
      "Python News",
      "Python Logo"
    ]
  }
]
```
