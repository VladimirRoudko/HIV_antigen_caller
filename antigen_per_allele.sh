


while read peptide count; do allele=$(grep "$peptide" hiv.frequent.hla.antigens.txt | awk '{print $6}' | sort | uniq | wc -l); echo "$peptide $allele" >> hiv.frequent.hla.antigens.per-allele.txt; done < hiv.frequent.hla.antigens.per-patient-allele.txt



