#!/home/abeck/.virtualenvs/k36/bin/python3

"""
from scapy.all import *

target = input("Informe um alvo (ip): ")
destport = input("Informe a porta de destino: ")

port = int(destport)

ans,unans=sr(IP(dst=target, ttl=(1, 30))/TCP(dport=port, flags="S"))
ans.summary(lambda s, r: r.sprintf("%IP.src%\t{ICMP:%ICMP.type%}\t{TCP:%TCP.flags%}"))
"""


"""
from scapy.all import *
hostname = input("Digite o destino: ")
for i in range(1, 28):
    pkt = IP(dst=hostname, ttl=i) / UDP(dport=33434)
    # Send the packet and get a reply
    reply = sr1(pkt, verbose=0)
    if reply is None:
        # No reply =(
        break
    elif reply.type == 3:
        # We've reached our destination
        print ("Done!", reply.src)
        break
    else:
        # We're in the middle somewhere
        print ("%d hops away: " % i , reply.src)
"""

# Essa foi a única implementação que funcionou adequadamente
import sys
import os
from scapy.all import sr1,IP,ICMP

if len(sys.argv) != 2:
    sys.exit('Usage: traceroute.py <remote host>')

# we start with 1
ttl = 1
while 1:
    p=sr1(IP(dst=sys.argv[1],ttl=ttl)/ICMP(id=os.getpid()), verbose=0)
    # if time exceeded due to TTL exceeded
    if p[ICMP].type == 11 and p[ICMP].code == 0:
        print (ttl, '->', p.src)
        ttl += 1
    elif p[ICMP].type == 0:
        print (ttl, '->', p.src)
        break