# coding: utf-8
import fire
import requests
from requests import Response
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.parse import urldefrag
import pprint
import re
import sys
import json


class Dora(object):

    def __init__(self):
        self.__searched_urls = set()
        self.__result = []

    def search(self, search_word: str, base_url: str, depth_limit: int=0):
        self.__search(search_word,base_url,depth_limit)
        print(json.dumps(self.__result, ensure_ascii=False))

    def __search(self, search_word: str, base_url: str, depth_limit: int=0):
        res: Response = requests.get(base_url)
        soup: BeautifulSoup = BeautifulSoup(res.content, 'lxml')
        title = soup.find('title').text
        found_search_words = self.__find_search_word(search_word,soup)
        if not found_search_words:
            return
        result = {}
        result['title'] = title
        result['url'] = base_url
        result['found_search_words'] = list(found_search_words)
        self.__result.append(result)
        depth_limit-=1
        if depth_limit < 0:
            return
        links = self.__find_links(base_url, soup)
        for link in links:
            self.__search(search_word,link,depth_limit)

    def __find_links(self, base_url: str, soup: BeautifulSoup):
        self.__searched_urls.add(base_url)
        domain_url = '{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(base_url))
        links = set()
        for link in soup.find_all("a"):
            link_url, fragment = urldefrag(urljoin(base_url, link.get("href")))
            if link_url.startswith(domain_url) and not link_url in self.__searched_urls:
                links.add(link_url)
                self.__searched_urls.add(link_url)
        return links

    def __find_search_word(self, search_word: str, soup:BeautifulSoup):
        result = set()
        compile = re.compile('('+search_word+')')
        for word in soup.find_all(text=compile):
            result.add(re.search(compile,word).group())
        return result

def main():
    fire.Fire(Dora)

