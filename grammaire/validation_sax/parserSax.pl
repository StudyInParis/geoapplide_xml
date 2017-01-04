#!/usr/bin/perl
###############
###SYNOPSIS####
###############
#
#Auteur : Ferguth Johan
#
#Date : 23/11/2016
#
#But : Extraire des donnees du fichier de tournage de film, parsing sax
#
#Usage : perl parserSax.pl <fichierTournage.xml> <fichierTournage.dtd>
#
#Exemple : perl parserSax.pl tournagesdefilmsparis2011.xml tournagesdefilmsparis2011.dtd
#
#Remarques : /
###############


use strict;
use warnings;
use 5.018;
use XML::LibXML::SAX;
use XML::LibXML;
use JSON;
#use Switch;
use Data::Dumper;
# Gestion de l'utf8
use utf8;
binmode(STDOUT,":encoding(UTF-8)");
# Mise a jour librairie perso
use MySAXHandler;
#push (@INC, "~/binPerl");
#require Lib::Gestion;
# Main

## Gestion des arguments 
usage() unless ((@ARGV == 2) and (-f $ARGV[0]) and (-f $ARGV[1]) );

my $file = shift;
my $fileHTML = $file;
$fileHTML=~ s!.*/(.*)!$1!g;
$fileHTML=~ s/(.*).xml/$1.html/;
my $dtdFile = shift;

# Validation selon la grammaire en dom
my $parser = XML::LibXML->new();
my $dtd = XML::LibXML::Dtd->new(
                        "SOME // Public / ID / 1.0",
                        "$dtdFile"
                                  );
my $tree = $parser->parse_file($file);
$tree->validate($dtd);
# si utilisation dans une application
#eval{$tree->validate($dtd)};
#say $@;


# Parsing en Sax
open(my $IN,"<", $file) or die "Erreur de flux : $!";
# Lors la création de l'objet on lui passe comme argument une référence vers un tableau qui contiendra les résultats
my @result=();
my $handler = MyHandler->new(\@result);
my $parserSax = XML::LibXML::SAX->new( Handler => $handler );
$parserSax->parse_file($IN);


my @json;
foreach my $tournage (@result)
{
	my @temp;
	foreach my $cle (sort{$a cmp $b}(keys %$tournage))
	{
		push(@temp,$$tournage{$cle});
#		say "$cle : $$tournage{$cle}";
	}
	my $json= to_json(\@temp,{utf8 => 1, pretty => 1});
	push(@json,$json);
}

#my $json = to_json(\@result);
#say $json;


foreach my $ligne(@json)
{
	say "$ligne,";
}

#Fonction(s)

## quitter si usage incorrect
sub usage
{	my $sep ="_"x40;
	my $usage = "Usage correct : perl $0 <fichierTournage.xml> <fichierTournage.dtd>";
	say $sep; 
	say $usage;
	say $sep; 
	exit;
}


