mkdir $mainfolder
cd $mainfolder
mkdir project datasets general_scripts bin 
cd project 
mkdir scripts bash input output logs >readme.txt >commands.txt 
cd bash 
mkdir runall.sh 
mkdir filter*sh 
cd .. 
cd .. 
cd datasets 
mkdir CASP9 CASP10 CASP11 human_reference_genome 
cd .. 
cd general_scripts 
mkdir pdb_scripts templates 
cd .. 
cd bin 
mkdir fastalen SVM_to_txt txt_to_SVM echo_both