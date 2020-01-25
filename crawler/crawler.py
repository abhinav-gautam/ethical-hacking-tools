#! /usr/env/bin python

import requests


def request(url):
    try:
        get_response = requests.get('http://' + url)
        return get_response
    except requests.exceptions.ConnectionError:
        pass


def discover_subdomains(base_url):
    with open('wordlist.txt', 'r') as word_list:
        with open('available_subdomains_' + base_url + '.txt', 'w') as result_file:
            for line in word_list:
                word = line.strip()
                target_url = word + "." + base_url
                response = request(target_url)
                if response:
                    print('[+] Subdomain Found --> '+target_url)
                    result_file.write(target_url+'\n')
    print('[+] Done')


def discover_directories(base_url):
    with open('directories_wordlist.txt', 'r') as word_list:
        with open('available_directories_' + base_url.split('/')[0] + '.txt', 'w') as result_file:
            for line in word_list:
                word = line.strip()
                target_url = base_url + '/' + word
                response = request(target_url)
                if response:
                    print('[+] Directory Found --> '+target_url)
                    result_file.write(target_url+'\n')
    print('[+] Done')


#discover_subdomains('google.com')
discover_directories('10.0.2.15/mutillidae')
