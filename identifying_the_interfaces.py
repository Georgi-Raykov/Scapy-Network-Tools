from scapy.arch import get_if_hwaddr
from scapy.interfaces import get_if_list

for iface in get_if_list():
    try:
        print(f"Interface: {iface}, MAC: {get_if_hwaddr(iface)}")
    except Exception as e:
        print(f"Interface: {iface}, Error: {e}")
