from __future__ import division
import numpy as np
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO
import sys
import subprocess
import os

# argv[1] - input file with cluster stats in one line.
# argv[2] - input file with epitope stats in columns
# argv[3] - input file with all predicted antigens
# argv[4] - input file with hla stats in USA population
# argv[5] - output file


stats = subprocess.check_output('grep "P" '+sys.argv[1]+'', shell=True)
output = open(sys.argv[5],"w")

for cluster in stats.splitlines():
	ID = cluster.split()[1]
	first = float(cluster.split()[2])
	second = float(cluster.split()[3])
	if first >= 0.5 and second < 0.1:
		epitope_stats = subprocess.check_output('grep -w "'+ID+'" '+sys.argv[2]+'', shell=True)
		top = 0
		top_epitope = "NA"
		top_hla = []
		hla_freq = [ 0 for i in range(16) ]
		hla_type = []
		hla_type.append("USA NMDP African")
		hla_type.append("USA NMDP African American")
		hla_type.append("USA NMDP Caribean Black")
		hla_type.append("USA NMDP Caribean Hispanic")
		hla_type.append("USA NMDP Chinese")
		hla_type.append("USA NMDP Filipino")
		hla_type.append("USA NMDP Hispanic South or Central American")
		hla_type.append("USA NMDP Japanese")
		hla_type.append("USA NMDP Korean")
		hla_type.append("USA NMDP Mexican or Chicano")
		hla_type.append("USA NMDP Middle Eastern or North Coast of Africa")
		hla_type.append("USA NMDP North American Amerindian")
		hla_type.append("USA NMDP South Asian Indian")
		hla_type.append("USA NMDP Southeast Asian")
		hla_type.append("USA NMDP Vietnamese")
		hla_type.append("USA NMDP European Caucasian")


		for line in epitope_stats.splitlines():
			epitope = line.split()[0]
			population = line.split()[3]
			if int(population) > int(top):
				top = population
				top_epitope = epitope
		top_epitope_hla = subprocess.check_output("grep -w '"+top_epitope+"' "+sys.argv[3]+" | awk '{print $6}' | sort | uniq", shell=True)
		for hla in top_epitope_hla.splitlines():
			top_hla.append(hla)
			hla_stats = subprocess.check_output('grep -w "'+hla+'" '+sys.argv[4]+'', shell=True)
			for line in hla_stats.splitlines():
				for i in range(len(hla_type)):
					if hla_type[i] == line.split("\t")[2]:
						hla_freq[i] = float(hla_freq[i]) + float(line.split("\t")[1])
		composed_hla = ""
		for item in top_hla:
			composed_hla = composed_hla + "," + item
		for i in range(len(hla_type)):
			output.write(ID+"\t"+str(first)+"\t"+top_epitope+"\t"+composed_hla+"\t"+str(hla_freq[i])+"\t"+hla_type[i]+"\n")


	if first >= 0.4 and second > 0.1:
                epitope_stats = subprocess.check_output('grep -w "'+ID+'" '+sys.argv[2]+'', shell=True)
                top = 0 
                top_epitope = "NA"
		second_epitope = "NA"
                top_hla = []
                hla_freq = [0] * 16
		hla_type = []
                hla_type.append("USA NMDP African")
                hla_type.append("USA NMDP African American")
                hla_type.append("USA NMDP Caribean Black")
                hla_type.append("USA NMDP Caribean Hispanic")
                hla_type.append("USA NMDP Chinese")
                hla_type.append("USA NMDP Filipino")
                hla_type.append("USA NMDP Hispanic South or Central American")
                hla_type.append("USA NMDP Japanese")
                hla_type.append("USA NMDP Korean")
                hla_type.append("USA NMDP Mexican or Chicano")
                hla_type.append("USA NMDP Middle Eastern or North Coast of Africa")
                hla_type.append("USA NMDP North American Amerindian")
                hla_type.append("USA NMDP South Asian Indian")
                hla_type.append("USA NMDP Southeast Asian")
                hla_type.append("USA NMDP Vietnamese")
                hla_type.append("USA NMDP European Caucasian")

                for line in epitope_stats.splitlines():
                        epitope = line.split()[0]
                        population = line.split()[3]
                        if int(population) > int(top):
                                top = population
                                top_epitope = epitope
		for line in epitope_stats.splitlines():
                        epitope = line.split()[0]
                        population = line.split()[3]
			difference = 7000
			if (int(top) - int(population)) > 0 and (int(top) - int(population)) < int(difference):
				difference = (int(top) - int(population))
				second_epitope = epitope

                top_epitope_hla = subprocess.check_output("grep -w '"+top_epitope+"' "+sys.argv[3]+" | awk '{print $6}' | sort | uniq", shell=True)
                second_epitope_hla = subprocess.check_output("grep -w '"+second_epitope+"' "+sys.argv[3]+" | awk '{print $6}' | sort | uniq", shell=True)
		for hla in top_epitope_hla.splitlines():
                        top_hla.append(hla)
                        hla_stats = subprocess.check_output('grep -w "'+hla+'" '+sys.argv[4]+'', shell=True)
                        for line in hla_stats.splitlines():
				for i in range(len(hla_type)):
                                	if hla_type[i] == line.split("\t")[2]:
                      		        	hla_freq[i] = float(hla_freq[i]) + float(line.split("\t")[1])

		for hla in second_epitope_hla.splitlines():
                        top_hla.append(hla)
                        hla_stats = subprocess.check_output('grep -w "'+hla+'" '+sys.argv[4]+'', shell=True)
                        for line in hla_stats.splitlines():
				for i in range(len(hla_type)):
                                	if hla_type[i] == line.split("\t")[2]:
                                        	hla_freq[i] = float(hla_freq[i]) + float(line.split("\t")[1])

                composed_hla = ""   
                for item in top_hla:
                        composed_hla = composed_hla + "," + item

                for i in range(len(hla_type)):
                        output.write(ID+"\t"+str(first)+","+str(second)+"\t"+top_epitope+","+second_epitope+"\t"+composed_hla+"\t"+str(hla_freq[i] / 2)+"\t"+hla_type[i]+"\n")


output.close()
