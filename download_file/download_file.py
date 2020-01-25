#! /usr/bin/env python

import requests


def download_file(url):
    get_response = requests.get(url)
    file_name = url.split('/')[-1]
    with open(file_name, "wb") as output_file:
        output_file.write(get_response.content)


download_file("https://www.rd.com/wp-content/uploads/2019/11/cat-10-e1573844975155-768x519.jpg")
