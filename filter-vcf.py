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
    parser.add_argument("-o", "--output_vcf", action="store",
            default="./output.vcf",
            help="Output VCF")
    parser.add_argument("-m", "--min", action="store",
            default=10, type=int,
            help="Minimum QUAL for alternate base")
    
    args = parser.parse_args()


output_handle = open(args.output_vcf,'w')
input_vcf = args.vcf
min_qual = args.min

print("Parsing VCF")

count_of_bad=0
count_of_good=0

with open(input_vcf,'r') as file_in:
    for line in file_in:
        if not ('#' in line):
            line=line.strip()
            cols=line.split('\t')
            qual=float(cols[5])
            if (qual <= min_qual):
                count_of_bad += 1
                continue
            else:
                count_of_good += 1
                output_handle.write(line + os.linesep) 
        else:
            output_handle.write(line + os.linesep) #write header lines

print("Found {:d} variant calls above min_qual of {:d}".format(int(count_of_good),min_qual))
print("Found {:d} that did not pass quality filter".format(int(count_of_bad)))

output_handle.close()

