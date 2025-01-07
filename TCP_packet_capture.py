from scapy.all import sniff
from scapy.layers.inet import TCP, IP


def process_http(packet):
    if packet.haslayer('TCP') and packet[TCP].dport == 80:
        print(f"HTTP заявка от {packet[IP].src} до {packet[IP].dst}")


sniff(filter="tcp port 80", prn=process_http, count=5)
