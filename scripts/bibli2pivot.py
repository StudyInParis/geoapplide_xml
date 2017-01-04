#!\C:\python34
# -*- coding: utf-8 -*-
import sys, math, re

fic = open("../donnees_xml/Bibliotheque.xml","r")
out = open("../donnees_xml/Bibliotheque_pivot.xml","w")
out.write(fic.readline())
out.write("<root>")
dico={}
elems = 0
for line in fic.readlines():
	i =0
	line=line.rstrip("\n")
	if "750" in line:
		arrs =line.split("<")
		arr=arrs[1].split(">")[1]
		if arr not in dico:
			dico[arr]=1
		else:
			dico[arr]+=1
print(dico)
elems +=1