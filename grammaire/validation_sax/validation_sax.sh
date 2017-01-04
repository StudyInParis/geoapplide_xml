#!/bin/bash
perl parserSax.pl ../../XML/fichiers_2xml/Bibliotheque.xml  ../validation_xml/Bibliotheque.dtd
perl parserSax.pl ../../XML/fichiers_2xml/cinemas.xml  ../validation_xml/cinemas2.dtd
perl parserSax.pl ../../XML/fichiers_2xml/restauration_france_entiere.xml  ../validation_xml/crous_propre.dtd
perl parserSax.pl ../../XML/fichiers_2xml/preservatifs.xml  ../validation_xml/distributeurspreservatifsmasculinsparis2012.dtd
perl parserSax.pl ../../XML/fichiers_2xml/fac.xml  ../validation_xml/fac.dtd
perl parserSax.pl ../../XML/fichiers_2xml/liste-des-cafes-a-un-euro.xml  ../validation_xml/liste-des-cafes-a-un-euro.dtd
perl parserSax.pl ../../XML/fichiers_2xml/liste-marches.xml  ../validation_xml/liste-marches2.dtd
perl parserSax.pl ../../XML/fichiers_2xml/OpenBeerMap.xml  ../validation_xml/OpenBeerMap.dtd
