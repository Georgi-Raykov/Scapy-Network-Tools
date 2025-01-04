from scapy.all import *

for ip in range(1,255):

    packet = sr1(IP(dst=f"192.168.0.{ip}")/ICMP(), timeout=2)
    if packet:
        print(f"192.168.1.{ip} is up")
    else:
        print(f"192.168.1.{ip} is down")