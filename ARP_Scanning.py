from scapy.all import *

arp_request = ARP(pdst="192.168.136.1/24")
broathcast = Ether(dst="ff:ff:ff:ff:ff:ff")

arp_request_broadcast = broathcast/arp_request

answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]
for element in answered_list:
    print(element[1].psrc)