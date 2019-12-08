#!/bin/bash

#SBATCH --account=bgmp          ### SLURM account which will be charged for the job
#SBATCH --partition=bgmp        ### Partition (like a queue in PBS)
#SBATCH --job-name=deduplicate      ### Job Name
#SBATCH --output=slurm-%j-%x.out         ### File in which to store job output
#SBATCH --time=0-01:00:00       ### Wall clock time limit in Days-HH:MM:SS
#SBATCH --nodes=1               ### Node count required for the job (usually 1)
#SBATCH --ntasks-per-node=1     ### Nuber of tasks to be launched per Node (usually 1)
#SBATCH --cpus-per-task=2       ### Number of cpus (cores) per task
#SBATCH --mail-user=abbiefayeolson@gmail.com
#SBATCH --mail-type=ALL

UMI=/projects/bgmp/afo/bi624/deduper/Deduper/files/STL96.txt

cd /projects/bgmp/afo/bi624/deduper/Deduper/scripts

/usr/bin/time -v ./olson_deduper.py -f /projects/bgmp/afo/bi624/deduper/Deduper/files/Dataset1.out.sort.sam -u $UMI -p 'False' -o Dataset_1
/usr/bin/time -v ./olson_deduper.py -f /projects/bgmp/afo/bi624/deduper/Deduper/files/Dataset2.out.sort.sam -u $UMI -p 'False' -o Dataset_2
/usr/bin/time -v ./olson_deduper.py -f /projects/bgmp/afo/bi624/deduper/Deduper/files/Dataset3.out.sort.sam -u $UMI -p 'False' -o Dataset_3

wc -l Dataset_1_deduplicated.out.sam
wc -l Dataset_2_deduplicated.out.sam
wc -l Dataset_3_deduplicated.out.sam

