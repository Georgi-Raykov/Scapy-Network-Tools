

from scapy.layers.inet import ICMP, IP, TCP, sr1

packet = IP(dst="8.8.8.8") / ICMP()

response = sr1(packet)

if response:
    response.show()


