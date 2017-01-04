#!/usr/bin/python3
#! coding: utf-8

"""
Module qui prend en entrée un fichier et crée une table de hachage avec les arrondissements et les loyers associés à chaque quartier de l'arr, la date de création des immeubles, la taille des appartements, fait la moyenne de tous ces nombres PAR ARRONDISSEMENT et les stocke en valeur dans un second dictionnaire
"""

import math
from pprint import pprint
def create_dic(fichier):
	fic = open(fichier,"r")
	useless_ligne = fic.readline()
	lignes = fic.readlines()
	dic = {}
	dic2 = {}
	for ligne in lignes:
		ligne = ligne.rstrip()
		tab_ligne = ligne.split(",")
		if int(tab_ligne[0]) < 10:
			(tab_ligne[0]) = "7500"+(tab_ligne[0])
		else:
			(tab_ligne[0]) = "750"+(tab_ligne[0])
		if tab_ligne[0] not in dic:
			dic[tab_ligne[0]] = float(tab_ligne[7])
			dic2[tab_ligne[0]] = 1
		else :
			dic[tab_ligne[0]] += float(tab_ligne[7])
			dic2[tab_ligne[0]] += 1
	for cle in sorted(dic):
		dic[cle] = int(dic[cle]/dic2[cle])
	return dic
