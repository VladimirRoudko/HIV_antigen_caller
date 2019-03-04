from Bio import SeqIO
from Bio.Seq import Seq 
from Bio.Seq import MutableSeq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_protein
import sys 
import subprocess
import os

folder = "netMHC2_hiv"
os.system('mkdir -p '+folder)
os.system('mkdir -p '+folder+'/'+sys.argv[1])

output = []
data = []

for seq_record in SeqIO.parse("per_patient/"+sys.argv[1]+".fasta", "fasta"):		# argv[1] - input file
	if len(seq_record.seq) >= 15:
		output.append(seq_record)
SeqIO.write(output, "per_patient/above.15."+sys.argv[1]+".fasta", "fasta")

list_HLA = subprocess.check_output('cat '+sys.argv[2], shell=True)	# argv[2] - file with HLA-II allele list
for allele in list_HLA.split('\n'):
	os.system('netMHC2 -a "'+allele+'" -f per_patient/above.15."'+sys.argv[1]+'".fasta -l 15 > "'+folder+'/'+sys.argv[1]+'/'+allele+'.hiv.MHCII.epitopes.output"')
my_excellist = subprocess.check_output('ls '+folder+'/'+sys.argv[1]+'/', shell=True)
for excel_file in my_excellist.split():
	my_input = open(folder+'/'+sys.argv[1]+'/'+excel_file,"r")
	my_allele = excel_file.split(".")[0]
	for line in my_input:
		try:
			if line.split()[0] == my_allele:
				try:
					ALLELE = line.split()[0]
					MPOS = line.split()[1]
					MKD = line.split()[6]					
					MSCORE = line.split()[7]
					MID = line.split()[9].split("_")[0]		
					MPEPTIDE = line.split()[2]			
					if float(MSCORE) <= 2:
						string = MID+" "+my_allele+" "+MPOS+" "+MPEPTIDE+" "+MSCORE+" "+MKD+"\n"
						data.append(string)
					if float(MKD) <= 500:
						string = MID+" "+my_allele+" "+MPOS+" "+MPEPTIDE+" "+MSCORE+" "+MKD+"\n"
						data.append(string) 
				except ValueError:
					continue
		except IndexError:
			continue
	my_input.close()

output = open(sys.argv[3],"w")				# output filename
for item in list(set(data)):
	output.write("%s" % item)
output.close()






