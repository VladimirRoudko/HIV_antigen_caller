

i=0
while read ID protein tool type1 type2 HLA peptide KD score 
do 
protein=$(echo $protein | awk -F'_' '{print $1}') 
echo ">$i.$ID.$protein.$HLA" >> hiv.frequent.hla.antigens.fasta
echo $peptide >> hiv.frequent.hla.antigens.fasta; 
i=$(($i+1))
done < hiv.frequent.hla.antigens.txt

