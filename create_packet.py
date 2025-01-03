from scapy.all import *

ip = IP(dst="www.example.com")
syn = TCP(dport=80, flags='S')

packet = ip/syn
send(packet)