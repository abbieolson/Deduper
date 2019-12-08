#!/usr/bin/env python


import argparse
import re

parser = argparse.ArgumentParser(description="This is a program for removing PCR duplicates.")

parser.add_argument("-f", "--file", help="Provide a sorted SAM file. We recommend samtools for this.", required=True, type=str)
parser.add_argument("-p", "--paired", choices=['True', 'False'], help="This parameter is for paired-end reads", required=True, type=str)
parser.add_argument("-u", "--umi", help="Provide a a list of known UMIs in a FASTQ format.", required=True, type=str)
parser.add_argument("-o", "--out", help="Name your output file.", required=False, type=str)

args = parser.parse_args()

FILE = args.file
UMI = args.umi
OUT = args.out
IF_PAIRED = args.paired

def bitwise_flag_fwd_reverse(bit_flag):
    '''A function for identifying forward and reverse reads'''
    if ((int(bit_flag) & 16) != 16): # forward strand
        return True
    elif ((int(bit_flag) & 16) == 16): # reverse strand
        return False

def read_parser(bit_flag, position, cig_string):
    '''A function that adjusts the CIGAR string for soft-clipping, insertions, and deletions'''
    positive = bitwise_flag_fwd_reverse(bit_flag)
    adjusted_position = 0
    if positive == True:
        start_S = re.search(r'^[0-9]+S', cig_string)
        if start_S == None:
            S_string = 0
            adjusted_position = position - S_string
        else:
            S_string = int((start_S.group(0)[:-1]))
            adjusted_position = position - S_string
        return adjusted_position, positive
    if positive == False:
        end_S = re.findall('([0-9]+)S$', cig_string)
        M_string = re.findall('([0-9]+)M', cig_string)
        N_string = re.findall('([0-9]+)N', cig_string)
        D_string = re.findall('([0-9]+)D', cig_string)
        if end_S == None:
            S = 0
            for letter in end_S:
                S += int(letter[:-1])
        if M_string == None:
            M = 0
            for letter in M_string:
                M += int(letter[:-1])
        if N_string == None:
            N = 0
            for letter in N_string:
                N += int(letter[:-1])
        if D_string == None:
            D = 0
            for letter in D_string:
                D += int(letter[:-1])
            adjusted_position = position + S + M + N + D
        return adjusted_position, positive

umi_list = [] # Initialize an empty list to store known UMIs, a list to store keys and values, and a counter for sorted chromosomes
storage_dict = {}
chromosome_counter = 1

sam_input = open(FILE, 'rt') # Open SAM file
raw_umi = open(UMI, 'rt') # Open file of known UMIs
final_sam = open(OUT + '_deduplicated.out.sam', 'w') # Deduplicated output file

for line in raw_umi: # Format raw UMI file, store in list
    line = line.strip().split()
    umi_list.append(line)

for line in sam_input: # Begin file iteration
    if line[0] == '@': # If just a header is detected, write to file
        final_sam.write(line)
    else:  # Use the findall() function of Python regex to detect known UMIs in the SAM file
        line = line.strip().split()
        found_umi = re.findall('[A-Z]+$', line[0])
        if found_umi not in umi_list:
            continue
        else:
            chromosome = line[2]
            bit_flag = int(line[1])
            position = int(line[3])
            cig_string = line[5]
            adjusted_position, positive = read_parser(bit_flag, position, cig_string)
            if chromosome != chromosome_counter:
                storage_dict = {}
            chromosome_counter = chromosome
            dict_key = (chromosome, adjusted_position) # Create a key of chromosome and left-most position for comparison
            if positive == True: # Forward read
                if dict_key not in storage_dict: # If the key is not identified in the SAM file, it hasen't been encountered yet and will be written to a file
                    storage_dict[dict_key] = []
                    storage_dict[dict_key].append(found_umi)
                    final_sam.write('\t'.join(line) + '\n')
                else: # If it has already been encountered, it's a PCR duplicate and will be omitted from the output file
                    if found_umi in storage_dict[dict_key]:
                        continue
                    else:
                        storage_dict[dict_key].append(found_umi)
                        final_sam.write('\t'.join(line) + '\n')
            if positive == False: # Reverse read
                if dict_key not in storage_dict: # If the key is not identified in the SAM file, it hasen't been encountered yet and will be written to a file
                    storage_dict[dict_key] = []
                    storage_dict[dict_key].append(found_umi)
                    final_sam.write('\t'.join(line) + '\n')
                else: # If it has already been encountered, it's a PCR duplicate and will be omitted from the output file
                    if found_umi in storage_dict[dict_key]:
                        continue
                    else:
                        storage_dict[dict_key].append(found_umi)
                        final_sam.write('\t'.join(line) + '\n')
final_sam.close()
