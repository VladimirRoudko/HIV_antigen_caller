from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO
import sys
import subprocess
import os

# argv1 - file with clusters
#argv2 - file with peptides
#argv3 - output file

cluster_ID = open(sys.argv[1], "r")
peptides = open(sys.argv[2], "r")
output = open(sys.argv[3],"w")

for record in cluster_ID:
	line_allele = "A " + record
	line_patient = "P " + record
	stats = subprocess.check_output('awk -v awkcluster="'+record+'" "$2==awkcluster" peptide.stats', shell=True)
	for stat in stats.split("\n"):
		line_allele = line_allele + " " + stat.split(" ")[2]
		line_patient = line_patient + " " + stat.split(" ")[3]
	
