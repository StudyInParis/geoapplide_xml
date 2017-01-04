package MyHandler;
use strict;
use warnings;
use Data::Dumper;
use 5.022;

my %hash=();
my $flag="";
my $id="";
my $refExt;

sub new 
{
	my $type = shift;
	$refExt = shift;
	return bless {}, $type;
}

sub start_element 
{
	my ($self, $element) = @_;
#	say "<$element->{Name}>";
	if($element->{Name} eq "tournage")
	{
		$flag=$element->{Name};
		$id=$element->{Attributes}->{"{}id"}->{Value};
#		say Dumper $element->{Attributes};
	}
	else
	{
		$flag=$element->{Name};
	}
}

sub end_element 
{
	my ($self, $element) = @_;
#	say "</$element->{Name}>";
	my %returnHash=();
	%returnHash=%hash;
	if($element->{Name} eq "tournage")
	{		
		%hash=();
		$flag="";
		push(@$refExt,\%returnHash);
	}
}

sub characters {
	my ($self, $characters) = @_;
	if($flag ne "")
	{
		if($flag eq "tournage")
		{
			$hash{$flag}=$id;
		}
		else
		{
			$characters->{Data}=~ s/\n//;
			$characters->{Data}=~ s/\r//;
			$hash{$flag}.=$characters->{Data};
		}
	}
}


1;
