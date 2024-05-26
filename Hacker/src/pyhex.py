#!/home/abeck/.virtualenvs/k36/bin/python3

import os
import sys

try:
	string = sys.argv[1]
	cmd = "echo -n"+string+"| xxd -ps | sed 's/[[:xdigit:]]\{2\}/\\\\x&/g'"
	os.system(cmd)
except IndexError:
	print("Informe uma string")
