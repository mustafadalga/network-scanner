#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import  ArgumentParser
import sys
from termcolor import colored
try:
	import scapy.all as scapy
except KeyboardInterrupt:
	pass

class Scanner():

	def __init__(self):
		self.about()
		self.script_desc()

	def arguman_al(self):
		parser = ArgumentParser(description=self.description,epilog=self.kullanim,prog=self.program)
		parser.add_argument("--hedef", dest="hedef", help="Hedef IP / IP aralik.")
		options = parser.parse_args()
		if not options.hedef:
			parser.error('[-] Lütfen bir hedef belirleyiniz,daha fazla bilgi için --help kullanın.')
		else:
			return options



	def scan(self,ip):
		print(colored("[+] Taranılan IP Aralığı:","green")+options.hedef+"\n")
		arp_istek=scapy.ARP(pdst=ip)
		broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
		arp_request_broadcast=broadcast/arp_istek
		answered_list=scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]

		client_list=[]
		for element in answered_list:
			client_dict={"ip":element[1].psrc,"mac":element[1].hwsrc}
			client_list.append(client_dict)
		return client_list


	def goruntule(self,sonuc_liste):
		print("IP\t\t\tMac Adresi\n-------------------------------------------")
		for client in sonuc_liste:
			print(client["ip"]+"\t\t"+client["mac"])

	def script_desc(self):
		self.program = "network_scanner"
		self.kullanim = """Ornek Kullanim: python network_scanner.py --hedef    10.0.2.1/24"""
		if sys.version_info[0] >= 3:
			self.description = "Python'un scapy modülü kullanılarak aynı ağda bulunan cihazların ip ve mac adreslerini listeyen script."
		else:
			self.description = unicode("Python'un scapy modülü kullanılarak aynı ağda bulunan cihazların ip ve mac adreslerini listeyen script.","utf8")
			self.kullanim = unicode(self.kullanim, "utf8")

	def about(self):
		print(colored("_   _      _                      _          _____                                 ", "green"))
		print(colored("| \ | |    | |                    | |        / ____|                                ", "green"))
		print(colored("|  \| | ___| |___      _____  _ __| | __    | (___   ___ __ _ _ __  _ __   ___ _ __ ", "green"))
		print(colored("| . ` |/ _ \ __\ \ /\ / / _ \| '__| |/ /     \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|", "green"))
		print(colored("| |\  |  __/ |_ \ V  V / (_) | |  |   <      ____) | (_| (_| | | | | | | |  __/ |   ", "green"))
		print(colored("|_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\    |_____/ \___\__,_|_| |_|_| |_|\___|_|   ", "green"))
		print(colored("# author      :", "green") + "Mustafa Dalga")
		print(colored("# linkedin    :", "green") + "https://www.linkedin.com/in/mustafadalga")
		print(colored("# github      :", "green") + "https://github.com/mustafadalga")
		print(colored("# title       :", "green") + "spider.py")
		print(colored("# description :","green") + "Python'un scapy modülü kullanılarak aynı ağda bulunan cihazların ip ve mac adreslerini listeyen script.")
		print(colored("# date        :", "green") + "21.02.2019")
		print(colored("# version     :", "green") + "1.0")
		print(colored("# ==============================================================================", "green"))

try:
	scanner=Scanner()
	options=scanner.arguman_al()
	tarama_sonuc=scanner.scan(options.hedef)
	scanner.goruntule(tarama_sonuc)
except:
	pass
