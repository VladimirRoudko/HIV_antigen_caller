from Bio import SeqIO
from Bio.Seq import Seq 
from Bio.Seq import MutableSeq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_protein
import sys 
import subprocess
import os
from Bio import pairwise2

source = open(sys.argv[1], "r")
epitope0="N"
clusters = []
iterator = 0
output = open(sys.argv[2],"w") 


for record in source:		# argv[1] - input file
	epitope1 = record.split(" ")[0]
	if epitope0 == "N":
		epitope0 = epitope1
		clusters.append(epitope0)
		
	else:
		flag = 0
		for item in clusters:
			score = pairwise2.align.globalxx(item, epitope1, score_only = True, one_alignment_only = True)
			if score == 8:
				flag = 1
				clusters.append(epitope1)
				break
		if flag == 0:
			for item in clusters:
				output.write(item+" "+str(iterator)+"\n")
			iterator = iterator + 1
			del clusters[:]
			clusters.append(epitope1)

output.close()
source.close()


