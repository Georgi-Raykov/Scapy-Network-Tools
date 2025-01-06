import random
from scapy.all import *
import time

from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import IP, UDP

target_domain = 'example.com'


def generate_ip():
    return '.'.join(str(random.randint(1, 255)) for _ in range(4))


def send_fast_flux_packet(target_domain):
    random_ips = [generate_ip() for _ in range(5)]

    ip = IP(dst='8.8.8.8')
    udp = UDP(dport=53)
    dns = DNS(rd=1, qd=DNSQR(qname=target_domain))

    dns_an = DNSRR(rrname=target_domain, rdata=random.choice(random_ips), ttl=60)
    dns.an = dns_an

    packet = ip / udp / dns
    send(packet, verbose=0)


while True:
    send_fast_flux_packet(target_domain)
    time.sleep(1)
