#!/home/abeck/.virtualenvs/k36/bin/python3

import socket
import subprocess

host = '127.0.0.1'
port = 443

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(b'\nHACK CMD:>>>')
#s.close