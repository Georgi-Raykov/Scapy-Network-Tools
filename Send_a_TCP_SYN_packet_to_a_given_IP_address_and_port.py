from scapy.all import *

syn_packet = IP(dst="192.168.36.208")/TCP(dport=80, flags='S')
response=sr1(syn_packet)

if response:
    response.show()

ack_packet = IP(dst="192.168.36.208")/TCP(dport=80, flags='A', ack=response.seq+1)
send(ack_packet)
