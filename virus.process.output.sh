
INPUT=$1
OUTPUT=$2
FLAG=$3

while read cluster size
do
grep -w "$cluster" "hiv.frequent.hla.antigens.clusters.txt" | awk '{print $1}' | while read epitope
do
grep $epitope "hiv.frequent.hla.antigens.txt" | awk '{print $6}' >> tmp.alleles.txt.$FLAG
grep -m 1 $epitope "hiv.frequent.hla.antigens.txt" | awk '{print $2}' | awk -F'_' '{print $1}' >> tmp.protein.txt.$FLAG
grep $epitope "hiv.frequent.hla.antigens.per-patient.txt" | awk '{print $2}' >> tmp.patients.txt.$FLAG
done

cat "tmp.alleles.txt.$FLAG" | sort | uniq | while read allele
do 
grep $allele "human.USA.hla.frequency.txt" | awk -F'\t' '{print $2}' >> tmp.frequences.txt.$FLAG
done

SUM=0
sum=0
while read frequence
do 
SUM=$(echo "$SUM + $frequence" | bc -l)
number=$(echo "1/$frequence" | bc -l)
sum=$(echo "$sum + $number" | bc -l)
done < tmp.frequences.txt.$FLAG
total=$(cat tmp.frequences.txt.$FLAG | wc -l)

harmonic=$(echo "scale=5; $total/$sum" | bc -l)
arithmetic=$(echo "scale=5; $SUM/$total" | bc -l)
protein=$(head -1 tmp.protein.txt.$FLAG)
patients=0
while read number
do
patients=$(( $patients + $number ))
done < tmp.patients.txt.$FLAG

fraction=$(echo "scale=5; $patients/7106" | bc -l)

echo "$cluster $protein $size $patients $fraction $harmonic $arithmetic" >> $OUTPUT

rm tmp.patients.txt.$FLAG
rm tmp.protein.txt.$FLAG
rm tmp.frequences.txt.$FLAG
rm tmp.alleles.txt.$FLAG

done < $INPUT



