
# $1 - filename with clusters
# $2 - output file


while read cluster_ID
do
line_allele=$(echo "A $cluster_ID")
line_patient=$(echo "P $cluster_ID")
awk -v awkcluster="$cluster_ID" '$2==awkcluster' peptide.stats | while read peptide ID allele_N patient_N 
do
line_allele=$(echo "$line_allele $allele_N")
line_patient=$(echo "$line_patient $patient_N")
echo $line_allele
done

echo $line_allele >> $2
echo $line_patient >> $2

done < $1

