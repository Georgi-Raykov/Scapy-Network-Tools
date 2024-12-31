from scapy.all import *
from scapy.layers.inet import IP, ICMP, TCP

pkt = IP(dst="8.8.8.8")/ICMP()  # ICMP (ping) пакет, насочен към 8.8.8.8
pkt.show()

pkt = IP(dst="8.8.8.8")/TCP(dport=80, flags="S")  # TCP пакет към порт 80 (за HTTP)
pkt.show()





