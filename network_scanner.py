#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scapy.all as scapy
import argparse

def arguman_al():
	parser=argparse.ArgumentParser()
	parser.add_argument("--hedef",dest="hedef",help="Hedef IP / IP aralığı.",)
	options=parser.parse_args()
	if not options.hedef:
		parser.error('[-] Lütfen bir hedef belirleyiniz,daha fazla bilgi için --help kullanın.')
	else:
		return options

def scan(ip):
	arp_istek=scapy.ARP(pdst=ip)
	broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast=broadcast/arp_istek
	answered_list=scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]

	client_list=[]
	for element in answered_list: 
		client_dict={"ip":element[1].psrc,"mac":element[1].hwsrc}
		client_list.append(client_dict)
	return client_list


def goruntule(sonuc_liste):
	print("IP\t\t\tMac Adresi\n-------------------------------------------")
	for client in sonuc_liste:
		print(client["ip"]+"\t\t"+client["mac"])


options=arguman_al()
tarama_sonuc=scan(options.hedef)
goruntule(tarama_sonuc)