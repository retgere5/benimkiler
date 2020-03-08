#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("apt-get install ike-scan")
os.system("clear")
os.system("figlet VPN KONTROL")

print("""

Vpn Kontrol Programına Hoşgeldin Bro

""")

hedefipsi = raw_input("Hedef İpsini Gir: ")

os.system("ike-scan " + hedefipsi)
