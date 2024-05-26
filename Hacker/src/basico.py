#!/home/abeck/.virtualenvs/k36/bin/python3


from scapy.all import *

ip = IP(dst="192.168.10.1")
tcp = TCP(dport=80)
pkt = ip/tcp
sr(pkt)
sr1(pkt)
pkt.show()

ip = IP(dst="192.10.10.1")
tcp = TCP(dport=80)/b"My payload"
pkt = ip/tcp
sr1(pkt)

#Criando um arquivo pcap
#--- $ tcpdump -i ens33 -w pcapfile.pcap

a = rdpcap("pcapfile.pcap")
a[3]
a[3].show()
a.hexdump()
a.hexraw()

pkts = sniff(count=10, iface="ens33")
wrpcap("C:/Users/beck_/OneDrive/Documents/eclipse-workspace/Hacker/src/tmp.pcap", pkts)