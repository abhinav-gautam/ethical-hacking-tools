#! usr/bin/env python

import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC")
    parser.add_option("-m", "--mac", dest="new_mac", help="New_MAC")
    (option, argument) = parser.parse_args()

    if not option.interface :
        parser.error("[-]Please enter interface")
    elif not option.new_mac:
        parser.error("[-]Please enter new MAC")
    return option


def change_mac(interface, new_mac):
    print("[+] Changing mac of " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC Address")


option = get_arguments()

current_mac = get_current_mac(option.interface)
print("Current MAC = "+str(current_mac))

change_mac(option.interface, option.new_mac)

current_mac = get_current_mac(option.interface)
if current_mac == option.new_mac:
    print("[+] MAC Address changed successfully to " + current_mac)
else:
    print("[-] MAC Address did not change")
print("[+] Done")
