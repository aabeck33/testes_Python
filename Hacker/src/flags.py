#!/home/abeck/.virtualenvs/k36/bin/python3


from scapy.all import *

dest = input("\nDestino: ")
destport = input("Porta de destino: ")
flag = input("Flags: ")

port = int(destport)
ip = IP(dst=dest)
tcp = TCP(dport=port, flags=flag)

pkt = ip/tcp

srloop(pkt, count=1)