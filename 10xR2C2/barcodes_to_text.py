import sys

# reads in a barcode.tsv file from 10x example: ATCAGTACAG-1 converts into a text file without the -1
barcode_file = sys.argv[1]
barcode_fasta = sys.argv[2]
bc_list=[]

for line in open(barcode_file,'r'):
	if line == '':
		continue
	else:
		barcode=line.split('-')[0]
		bc_list.append(barcode)

new_file = open(barcode_fasta,'w')

for i in range(len(bc_list)):
	new_file.write(bc_list[i] + '\n')