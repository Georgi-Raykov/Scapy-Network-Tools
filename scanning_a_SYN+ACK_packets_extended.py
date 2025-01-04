from scapy.all import *
from scapy.layers.inet import IP, TCP


def scan_ports(ip_target, start, end, report_file="scan_report_file.txt"):
    with open(report_file, 'w') as report:
        report.write(f"Port scan report for {ip_target}\n")
        report.write('=' * 50 + "\n")

        for port in range(start, end):
            packet = IP(dst='192.168.0.1') / TCP(dport=port, flags='S')

            response = sr1(packet, timeout=2)

            if response:
                if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
                    print(f"Port 80 is open!")
                    response.show()
                    ack_packet = IP(dst='192.168.0.1') / TCP(dport=80, flags='A', seq=response.ack,
                                                             ack=response.seq + 1)
                    send(ack_packet)
                elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
                    print(f"Port 80 is closed!")
            else:
                print("No response received")

            report.write('=' * 50 + '\n')
            report.write("Scan complete\n")


scan_ports('192.168.0.1', 20, 80)
# Този пакет може да се изпрати в контекста на опит за установяване на TCP сесия.
