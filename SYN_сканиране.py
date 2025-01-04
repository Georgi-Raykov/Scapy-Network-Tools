from scapy.all import *
from scapy.layers.inet import IP, TCP

ip_address = '192.168.0.1'

for port in range(20, 80 + 1):

    packet = IP(dst=ip_address)/TCP(dport=port, flags='S')
    response = sr1(packet, timeout=20)

    if response.haslayer(TCP) and response.getlayer(TCP).flags == 0X12:

        print(f"Port: {port} is open!")
    elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0X14:
        print(f"Port {port} is closed!")
    else:
        print(f"Port {port} is filtered or no response")