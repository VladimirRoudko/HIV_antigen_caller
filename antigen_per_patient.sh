

while read peptide count; do patients=$(grep "$peptide" hiv.frequent.hla.antigens.txt | awk '{print $1}' | sort | uniq | wc -l); echo "$peptide $patients" >> hiv.frequent.hla.antigens.per-patient.txt; done < hiv.frequent.hla.antigens.per-patient-allele.txt


