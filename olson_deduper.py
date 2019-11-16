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
















import re

#should nicely separate CIGAR entries
cigar_pat = re.compile(r"\d+[MIDNSHP=X]{1}")

def cigar2end( left,cigar ):
  """Return right-most position of aligned read."""
  #store info about each CIGAR category
  counts={ "M":0, #M 0 alignment match (can be a sequence match or mismatch)
           "I":0, #I 1 insertion to the reference
           "D":0, #D 2 deletion from the reference
           "N":0, #N 3 skipped region from the reference
           "S":0, #S 4 soft clipping (clipped sequences present in SEQ)
           "H":0, #H 5 hard clipping (clipped sequences NOT present in SEQ)
           "P":0, #P 6 padding (silent deletion from padded reference)
           "=":0, #= 7 sequence match
           "X":0, #X 8 sequence mismatch
        }
  #split cigar entries
  for centry in cigar_pat.findall(cigar):
    ccount  = int(centry[:-1])
    csymbol = centry[-1]
    counts[csymbol] = ccount
  #get number of aligned 'reference' bases
  aligned = counts["M"] + counts["D"] + counts["N"] #+ counts["="] + counts["X"]
  right   = left + aligned
  return right
