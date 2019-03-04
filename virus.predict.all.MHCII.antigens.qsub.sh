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

mkdir -p "MHCII_epitopes"

# Predict antigens:
python virus.get.all.MHCII.epitopes.py "$sample" "human_mhcII.txt" "MHCII_epitopes/$sample.hiv.antigen.txt"




