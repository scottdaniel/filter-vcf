#!/usr/bin/env python3
import sys
import argparse
import os

if __name__ == "__main__":
    parser = \
    argparse.ArgumentParser(description="Script to filter vcfs")
    parser.add_argument("-v", "--vcf", action="store",
            default="./sample.vcf",
            help="VCF file to filter")
    parser.add_argument("-o", "--output-vcf", action="store",
            default="./output.vcf",
            help="Output VCF")
    parser.add_argument("-m", "--min", action="store",
            default=10, type=Int,
            help="Minimum QUAL for alternate base")
    
    args = parser.parse_args()


output_vcf = args.output-vcf
input_vcf = args.vcf
min_qual = args.min

print("First get read_ids below max_score")

lowqual={}
counter1=0

for line in file_in:
    if not ('#' in line):
        line=line.strip()
        cols=line.split('\t')
        read_id=cols[0]
        try:
            score=int(cols[-1])
        except ValueError as exception:
            print("Bad line is here, continuing anyway")
            continue
        if (score < max_score):
            lowqual.update({read_id:score})
            counter1 += 1

print("{:s} had {:d} read_ids that were below {:d}".format(file_in,int(counter1),max_score))

fastq_files={}

#Only need to get DNA_3*clipped files for DNA_3_simple.txt (and same for 1,2,4)
prefix=file_in.name.split('_')[1]

#building list of files
for dirpath,dirnames,files in os.walk(fastq_dir):
    for fname in files:
        if fname.endswith('clipped') and fname.split('_')[1]==prefix:
            fastq_files[fname] = os.sep.join([dirpath,fname])

print("List of files is {:s}".format(fastq_files))

for fastq_name,fastq_path in fastq_files.iteritems(): #iterate through fastqs
    shortname = fastq_name.split('.')[0] #only first "word" before period
    if not os.path.exists(os.path.join(output_dir,shortname)): #check for dir
        os.makedirs(os.path.join(output_dir,shortname)) #create if not there
    output = open(os.path.join(output_dir,shortname,"lowqual.fastq"),'w') #open output file
    print("Outputting to {:s}".format(output.name))
    fqrecords=SeqIO.index(fastq_path,"fastq")
    counter2=0
    for hwis in lowqual.iterkeys(): #iterate through records in fasta
        try:
            fqrecords[hwis]
        except KeyError as exception: #if record isn't found we keep searching
            continue
        SeqIO.write(fqrecords[hwis],output,"fastq") #if found we write out
        counter2 += 1
    print("Finished getting {:d} records from {:s}".format(int(counter2),fastq_name))
    fqrecords.close() #good memory citizen even though i think python has garbage collection
    output.close()

file_in.close()

