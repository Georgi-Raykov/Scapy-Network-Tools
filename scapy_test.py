from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr

# Създаване на пакет
pkt = IP(dst="google.com")/TCP(dport=80)

# Изпращане на пакет и изчакване на отговор (sr)
answer = sr(pkt, timeout=2, verbose=2)

# Отговор от целевия хост
print(answer)




