from scapy.all import *
from scapy.layers.l2 import ARP, Ether

ip_range = '192.168.0.0/24'

arp_request = ARP(pdst=ip_range)

ether = Ether(dst='ff:ff:ff:ff:ff:ff')

packet = ether / arp_request

result = srp(packet, timeout=2, verbose=0)[0]
devices = []

for sent, receive in result:
    devices.append({'IP': receive.psrc, 'MAC': receive.hwsrc})

with open('report_file.txt', 'w') as f:
    f.write("Founded devices:\n")
    f.write('='* 100 + '\n')

    for device in devices:
        f.write(f"IP Address: {device['IP']}, MAC Address: {device['MAC']}\n")

        f.write('=' * 100 + '\n')