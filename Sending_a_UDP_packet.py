from scapy.all import *
from scapy.layers.inet import UDP, IP

ip = IP(dst='192.168.29.153')

udp = UDP(dport=53)

packet = ip/udp

send(packet)
packet.show()