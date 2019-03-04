#! /bin/sh
#$ -S /bin/bash
#$ -pe smp 1
#$ -cwd
#$ -N antigen_virus
#$ -e log/
#$ -o log/

. ~/.bashrc
. ~/.bash_profile

exec 1>log_neoantigen_frameshift.out
exec 2>log_neoantigen_frameshift.err

sample=$(awk NR==$SGE_TASK_ID virus.protein_per_patient.list)
sample=$(echo $sample | awk 'BEGIN{FS=OFS="."} {NF--; print}')

mkdir -p "antigens"

# Predict antigens:
python virus.peptide-to-antigen.py "$sample" "per_patient" "human_USA_frequent_hla.txt" "antigens/$sample.hiv.antigen.txt"





