#!/usr/bin/python3
#! coding:utf-8

"""
MODELISATION XML PIVOT-LIKE de BIBLIOTHEQUES.XML.
On récupère dans le xml bibliothèques les éléments (chaque enfant de <root>), on les stocke dans une
table de hachage et on va chercher l'arrondissement dans chaque valeur de la balise enfant, on en fait la clé
d'un second dictionnaire qui a comme valeur le reste du contenu de toutes les balises enfant contenant l'arrondissement
où chaque valeur de la clé est une liste (tableau) on parcourt ensuite chaque clé, et pour chaque liste de chaque clé, pour chaque élément, si cet élément contient les balises
qui nous intéressent, on les écrit dans le  output.)

!!! IL FAUT INSTALLER GEOCODER !!! bonne chance...
"""


import sys
import math
import geocoder
from pprint import pprint
def open_and_dic_and_dic2(fichier):
    fic = open(fichier,"r")
    dico = {}
    dico2 = {}
    num_l=0
    lines =fic.readlines()
    for line in lines:
        num_l+=1
        if "<elem" in line:
            dico[line] = lines[num_l:num_l+8]
    for cle in dico:
        for balise in dico[cle]:
            if "750" in balise:
                if balise not in dico2:
                    dico2[balise] = [dico[cle]]
                else:
                    dico2[balise] += [dico[cle]]
    return dico2
def output(fichier_out,fichier):
    out = open(fichier_out,"w")
    out.write("<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"no\"?>\n")
    out.write("<root>\n")
    dico2 = open_and_dic_and_dic2(fichier)
    num_bib = 0
    for cle in dico2:
        clef = cle.split("<")[1].split(">")[1]
        out.write('\t<arrondissement num ="'+clef+'">\n')
        for item in dico2[cle]:
            num_bib +=1
            out.write('\t\t<element id="'+str(num_bib)+'" type="bibli">\n')
            for balise in item:
                if"Designation" in balise:
                    balise = asciisation(balise)
                    name = balise.split("<")[1].split(">")[1]
                    out.write("\t\t\t<nom>"+name.lower()+"</nom>\n")
                if "voie" in balise:
                    for bal in item:
                        if "num" in bal:
                            balises = balise.split("<")[1].split(">")[1]
                            bals = bal.split("<")[1].split(">")[1]
                            adresse = bals+", "+balises.lower()
                            out.write("\t\t\t<adresse>"+adresse+"</adresse>\n")
                            g=geocoder.google(adresse)
                            out.write("\t\t\t<longitude>"+str(g.lng)+"</longitude>\n")   
                            out.write("\t\t\t<latitude>"+str(g.lat)+"</latitude>\n")
            out.write("\t\t</element>\n")
        out.write("\t</arrondissement>\n")
    out.write("</root>")
def asciisation(string):
    if 'È' in string or 'É' in string:
        string = string.replace('É','e')
        string = string.replace('È','e')
    return string
if __name__=='__main__':
    output("../XML/fichiers_2xml/Bibliotheques_modele.xml","../XML/fichiers_2xml_pivot/Bibliotheque.xml")
