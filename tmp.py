from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO
import sys
import subprocess
import os

for seq_record in SeqIO.parse("conserved_vaccine.fasta", "fasta"):
	for i in range(0, len(seq_record.seq) - 9 + 1):
		try:
			my_match = subprocess.check_output('grep -m 1 -w '+str(seq_record.seq[i:i+9])+' hiv.frequent.hla.antigens.epitopes-clusters-allele-patients.txt', shell=True)
		except subprocess.CalledProcessError:
			my_match = "NA"
		subprocess.check_output('echo "'+seq_record.id+' '+my_match+'" >> matches.txt', shell=True)

