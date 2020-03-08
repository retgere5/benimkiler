#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PORT TARAMA")

print("""
Port Tarama Programına Hoşgeldin Bro

1) Hızlı Tarama
2) Servis Ve Version Bilgisi
3) İşletim Sistemi Bİlgisi

""")

islemnumarasi = raw_input("İşlem Numarası Girin: ")

if(islemnumarasi == "1"):
	hedefipsi = raw_input("Hedefin İpsini Girin: ")
	os.system("nmap " + hedefipsi)

elif(islemnumarasi == "2"):
	hedefipsi = raw_input("Hedefin İpsini Gİrin: ")
	os.system("nmap -sS -sV " + hedefipsi)

elif(islemnumarasi == "3"):
	hedefipsi = raw_input("Hedefin İpsini Girin: ")
	os.system("nmap -O " + hedefipsi)

else:
	print("Hatalı Tuşlama Yaptınız!!!")
