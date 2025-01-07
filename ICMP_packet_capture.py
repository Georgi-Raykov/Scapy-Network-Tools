from scapy.all import sniff


def process_packet(packet):
    if packet.haslayer('ICMP'):
        print(f"Capture packet from {packet['IP'].src} to {packet['IP'].dst}")


sniff(filter='icmp', prn=process_packet, timeout=10)
