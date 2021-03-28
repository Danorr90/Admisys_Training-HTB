#Source https://xael.org/pages/python-nmap-en.html
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

	r = input(" 	1- Scan réseau\n	2- Détection de vulnérabilité\n    3- Exit\n	Veuillez entrer un numéro : ")

	if r =='1':
		scan()

	if r =='2':
		vulnirability()

	if r =='3':
		exit()

	else:
		print("Choisissez un bon numéro de commande 1, 2, ou 3")
		return main()


def scan():
	save = input("Consulter sur un rapport ? (o/n)")
	if save == 'o':
		fileSource = open("scan.txt", "w")
		print("******************************************************")
		print("*		    Scan réseau			     				 *")
		print("******************************************************")
		ip = input("\nVeuillez entrer une adresse IP: ")
		nm.scan(ip, '1-1024')
		print(nm.scaninfo(), file=fileSource)
		print(nm[ip].keys(), file=fileSource)
		print(nm[ip].all_protocols(), file=fileSource)
		fileSource.close()
	elif save == 'n':
		print("******************************************************")
		print("*		    Scan réseau			     				 *")
		print("******************************************************")
		ip = input("\nVeuillez entrer une adresse IP: ")
		nm.scan(ip, '1-1024')
		print(nm.scaninfo())
		print(nm[ip].keys())
		print(nm[ip].all_protocols())
	else:
		print("erreur de saisie ! \n")
		print("*******************************************************")
		print("					Menu principal")
		print("*******************************************************")
	return main()

def vulnirability():
	save = input("Consulter sur un rapport ? (o/n)")
	if save == 'o':
		print("******************************************************")
		print("*		  Détection de vulnérabilité         		 *")
		print("******************************************************")
		ip = input("\nVeuillez entrer une adresse IP: ")
		fileSource = open("vuln.txt", "w")
		print(os.system('nmap -T4 -A -v ' + ip), file=fileSource)
		fileSource.close()
	elif save == 'n':
		print("******************************************************")
		print("*		  Détection de vulnérabilité         		 *")
		print("******************************************************")
		ip = input("\nVeuillez entrer une adresse IP: ")
		print(os.system('nmap -T4 -A -v ' + ip))
	else:
		print("erreur de saisie ! \n")
		print("*******************************************************")
		print("					Menu principal")
		print("*******************************************************")
	return main()

if __name__ == '__main__':
	main()

"""
	 	 ________
		 \______ \ _____    ____   ___________ 
		  |    |  \\__  \  /    \ /  _ \_  __ \
		  |    `   \/ __ \|   |  (  <_> )  | \/
		 /_______  (____  /___|  /\____/|__|
                 		 \/     \/     \/ 

	                     .^. .  _ 
	                    /: ||`\/ \~  , 
	                , [   &    / \ y' 
	                {v':   `\   / `&~-, 
	                'y. '    |`   .  ' / 
	                \   '  .       , y 
	                v .        '     v 
	                V  .~.      .~.  V 
	                : (  0)    (  0) : 
	                 i `'`      `'` j 
	                  i     __    ,j 
	                   `%`~....~'& 
	                <~o' /  \/` \-s, 
	                 o.~'.  )(  r  .o ,. 
	                o',  %``\/``& : 'bF 
	               d', ,ri.~~-~.ri , +h 
	               `oso' d`~..~`b 'sos`
	                    d`+ II +`b 
	                    i_:_yi_;_y
                        """