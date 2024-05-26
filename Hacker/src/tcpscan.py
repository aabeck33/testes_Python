#!/home/abeck/.virtualenvs/k36/bin/python3


from scapy.all import *

target = input("Informe um host: ")
flag = input("Informe uma Flag: ")


res, unans = sr(IP(dst=target)/TCP(flags=flag,dport=(1,1024)))

res.show(lfilter=lambda s,r: (r.haslayer(TCP) and (r.getlayer(TCP).flags & 2)))