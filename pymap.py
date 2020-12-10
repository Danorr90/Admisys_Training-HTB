#!/usr/bin/python3
#Source https://xael.org/pages/python-nmap-en.html#:~:text=python-nmap%20is%20a%20python,can%20even%20be%20used%20asynchronously
#pip install python-nmap

import nmap
import os

nm = nmap.PortScanner()

print("******************************************************")
print("* _______________.___.  _____      _____ __________  *")
print("* \______   \__  |   | /     \    /  _  \\______   \  *")
print("*  |     ___//   |   |/  \ /  \  /  /_\  \|     ___/ *")
print("*  |    |    \____   /    Y    \/    |    \    |     *")
print("*  |____|    / ______\____|__  /\____|__  /____|     *")
print("*            \/              \/         \/           *")
print("******************************************************")

def main():
	
	r = input(" 	1- Scan réseau\n	2- Détection de vulnérabilité\n 	3- Exploit\n\n		Veuillez entrer un numéro : ")
	
	if r =='1':
		print("******************************************************")
		print("*		    Scan réseau			     *")
		print("******************************************************")
		ip = input("\nVeuillez entrer une adresse IP: ")
		nm.scan(ip , '1-1024')
		print(nm.scaninfo())
		print(nm[ip].keys())
		print(nm[ip].all_protocols())
	elif r =='2':
		print("******************************************************")
		print("*		  Détection de vulnérabilité         *")
		print("******************************************************")
		ip = input("\nVeuillez entrer une adresse IP: ")
		print(os.system('nmap -sV --script=default ' +ip))
	elif r =='3':
		os.system('msfconsole')
	else:
		print("Choisissez un bon numéro de commande 1, 2 ou 3")


if __name__ == '__main__':
	main()
