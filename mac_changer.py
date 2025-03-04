#!usr/bin/env python3

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "-mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if options.interface is None:
        parser.error("[-] Please specify an interface, use --help for more information.")
    elif options.new_mac is None:
        parser.error("[-] Please specify a new MAC, use --help for more information.")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.new_mac)


# ifconfig eth0 down
# ifconfig eth0 hw ether 22:33:44:55:66:77
# ifconfig eth0 up

# python/python3 mac_changer.py --interface eth0 --mac 22:33:44:55:66:77
# python/python3 mac_changer.py --i eth0 --m 22:33:44:55:66:77