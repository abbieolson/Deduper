#!/usr/bin/env python


# import argparse
# import re
#
# parser = argparse.ArgumentParser(description="Program for demultiplexing")
#
# parser.add_argument("-f", "--file", help="", required=True, type=str)
# parser.add_argument("-p", "--paired", help="", required=True, type=str)
# parser.add_argument("-u", "--umi", help="", required=True, type=str)
# parser.add_argument("-h", "--help", help="", required=True, type=str)
#
# args = parser.parse_args()
#
#
# FILE = args.file
# PAIRED = args.paired
# UMI = args.umi
# HELP = args.help


# read in the Bioo barcode indices file and initialize a dictioary

qname_fi = '/home/afo/bgmp/bi624/deduper/Deduper/STL96.txt'

raw_qname_list = []
all_qname = []
qname_dict = {}

raw_qname = open(qname_fi, 'rt')

# currently a list of lists
lines = raw_qname.readlines()
for x in lines:
    qname = x.strip().split()
    raw_qname_list.append(barcode)

# creates list of strings
for x in raw_bc_list:
    all_barcodes.append(''.join(x))


print(all_barcodes)
