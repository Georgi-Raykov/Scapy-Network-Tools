from scapy.all import *
from scapy.layers.l2 import ARP

packet = ARP(pdst='192.168.0.1')

send(packet)
packet.show()