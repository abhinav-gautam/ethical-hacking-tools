#! /usr/env/bin python

import requests
import urlparse
import re

target_url = 'http://10.0.2.17/mutillidae/'
target_links = []


def extract_links(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', str(response.content))


def crawl(url):
    href_links = extract_links(url)
    for link in href_links:
        link = urlparse.urljoin(url, link)
        if '#' in link:
            link = link.split('#')[0]
        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)


crawl(target_url)

