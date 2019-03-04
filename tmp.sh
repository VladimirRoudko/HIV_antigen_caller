while read peptide clusterID allele_N
do
#echo $clusterID
patient_N=$(grep -w "^$peptide" hiv.frequent.hla.antigens.per-patient.txt | awk '{print $2}')
echo "$peptide $clusterID $allele_N $patient_N" >> merged.txt
#echo -e "$line $allele_N\n"
done < hiv.frequent.hla.antigens.clusters-allele.txt

