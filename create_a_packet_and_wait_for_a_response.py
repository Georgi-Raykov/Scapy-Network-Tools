from scapy.all import *

response = sr1(IP(dst="www.example.com")/ICMP())
response.show()