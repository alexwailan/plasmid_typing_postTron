#!/usr/bin/env python3
import argparse
import sys
import os

parser = argparse.ArgumentParser(
	description = 'Simply preparing the fastq files',
	usage = 'Plasmid_typing_postTron [options] file_of_trait_fastqs identity_perc Date')
parser.add_argument('file_of_trait_fastqs', help='File of filenames of each trait isolate')
parser.add_argument('identity_perc', help='Identity percentage for blastn')
parser.add_argument('Date', help='Date of analysis for output naming e.g. 150417')
options = parser.parse_args()


date = options.Date
identity_perc = options.identity_perc
trait_infile = options.file_of_trait_fastqs

with open(trait_infile, "r") as inputdata:
    for i in inputdata:
        print(i) #to see what is going on here?
        #os.system('blastn -query plasmidFinder_16032017.fa -subject spades_'+i+'/contigs.fasta -perc_identity '+identity_perc+' -outfmt "10 qaccver saccver pident length mismatch gapopen qlen qstart qend slen sstart send evalue bitscore nident ppos" > '+i+'_plasmidfinder16032017_blast_results_'+date+'.csv')
        