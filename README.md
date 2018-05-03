# Filter-vcf
Simple script that filters a vcf file based on quality of given alternate allele (the 6th column of .vcf file)

## Steps
* `wget https://repo.continuum.io/archive/Anaconda3-5.0.1-MacOSX-x86_64.sh`
* `bash Anaconda3-5.0.1-MacOSX-x86_64.sh`
* `./filter-vcf.py -v sample.vcf -o output.vcf -m 10`
