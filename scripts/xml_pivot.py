#!/usr/bin/python3
# coding: utf-8

"""
Prend en entrée chaque xml au format xml_pivot et sort un xml avec tous les éléments à l'intérieur des balises de chaque arrondissement
Ajoute en attribut les loyers (voir module loyers) dans chaque balise <arrondissement>
"""
import re
from loyers import create_dic
from pprint import pprint
def open_and_dic(fichier,dic):
	fic = open(fichier,'r')
	lines = fic.readlines()
	num_l=0
	for line in lines:
		num_l +=1
		#print(num_l)
		if "<arron" in line:
			arr = line.split('"')[1]
			for ligne in lines[num_l:]:
				if "</arr" in ligne:
					break
				if arr not in dic:
					dic[arr] = []
				dic[arr] += [ligne]
	return dic
def out_xml(dico):
	fic = open("../XML/xml_pivot/xml_pivot.xml",'w')
	fic.write("<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"no\"?>\n<root>\n")
	compteur = 0
	dic2 = create_dic("../data/CSV/encadrement_loyers_paris.csv")
	for cle in sorted(dico):
		fic.write("\t<arrondissement num=\""+cle+"\" loyer=\""+str(dic2[cle])+"\">\n")
		for ligne in dico[cle]:
			if "<elem" in ligne:
				compteur +=1
				ligne = re.sub(r"[0-9]+",str(compteur),ligne)
			if "&" in ligne:
				ligne =ligne.replace('&',"&amp;")
			fic.write(ligne)
		fic.write("\t</arrondissement>\n")
	fic.write("</root>")
if __name__=='__main__':
	dic = {}
	dic = open_and_dic("../XML/fichiers_2xml_pivot\cinemas-a-paris_pivot.xml",dic)
	dic.update(open_and_dic("../XML/fichiers_2xml_pivot/Bibliotheque_modele.xml",dic))
	dic.update(open_and_dic("../XML/fichiers_2xml_pivot/distributeurspreservatifsmasculinsparis2012_pivot.xml",dic))
	dic.update(open_and_dic("../XML/fichiers_2xml_pivot/liste_des_marches_de_quartier_a_paris_pivot.xml",dic))
	dic.update(open_and_dic("../XML/fichiers_2xml_pivot/liste-des-cafes-a-un-euro_pivot.xml",dic))
	dic.update(open_and_dic("../XML/fichiers_2xml_pivot/openbeermap_pivot.xml",dic))
	dic.update(open_and_dic("../XML/fichiers_2xml_pivot/crous_restauration_france_entiere_pivot.xml",dic))
	
	#pprint(dic)
	out_xml(dic)
