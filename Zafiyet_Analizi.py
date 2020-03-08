#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Zafiyet Analizi")

print("""
Zafiyet Analizi Programına Hoşgeldin Bro
""")

hedefipsi = raw_input("Hedef İpsini Girin: ")

os.system("nikto -h " + hedefipsi)

print("""
Bitti Bro :)
""")
