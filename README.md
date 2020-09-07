# dora

> A simple scraping CLI tool

## Futures

- Simple usage
- Scraping with regular expression
- Deep scraping option

## Installation

- git clone
- ```poetry install```

## Usage

Scraping [NVD (NATIONAL VULNERABILITY DATABASE)](https://nvd.nist.gov/) Last 20 Scored Vulnerability IDs & Summaries

```
% poetry run dora search "CVE-[0-9]{4}-[0-9]{4,12}" https://nvd.nist.gov/ | jq . 
[
  {
    "title": "\r\n\tNVD - Home\r\n",
    "url": "https://nvd.nist.gov/",
    "found_search_words": [
      "CVE-2018-0237",
      "CVE-2020-3505",
      "CVE-2020-5622",
      "CVE-2018-0239",
      "CVE-2020-20625",
      "CVE-2018-0324",
      "CVE-2020-24618",
      "CVE-2018-0267",
      "CVE-2018-0266",
      "CVE-2020-24706",
      "CVE-2020-7665",
      "CVE-2020-17465",
      "CVE-2020-13469",
      "CVE-2018-0288",
      "CVE-2018-0245",
      "CVE-2020-7666",
      "CVE-2018-0269",
      "CVE-2018-0278",
      "CVE-2018-0279",
      "CVE-2018-0228"
    ]
  }
]
```

## Help

```
% poetry run dora search --help

NAME
    dora search - scraping by search_word(regular expression)

SYNOPSIS
    dora search SEARCH_WORD BASE_URL <flags>

DESCRIPTION
    scraping by search_word(regular expression)

POSITIONAL ARGUMENTS
    SEARCH_WORD
    BASE_URL

FLAGS
    --depth_limit=DEPTH_LIMIT

NOTES
    You can also use flags syntax for POSITIONAL ARGUMENTS
```