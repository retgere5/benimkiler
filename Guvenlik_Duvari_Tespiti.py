#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet GUVENLIK DUVARI TESPITI")
print("""
GUVENLIK DUVARI TESPITI PROGRAMINA HOŞGELİNİZ
""")

site = raw_input("Hedef Siteyi Giriniz: ")
os.system("wafw00f " + site)
