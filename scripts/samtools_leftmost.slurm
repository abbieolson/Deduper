#!/bin/bash

#SBATCH --account=bgmp          ### SLURM account which will be charged for the job
#SBATCH --partition=bgmp        ### Partition (like a queue in PBS)
#SBATCH --job-name=samtools      ### Job Name
#SBATCH --output=slurm-%j-%x.out         ### File in which to store job output
#SBATCH --time=0-36:00:00       ### Wall clock time limit in Days-HH:MM:SS
#SBATCH --nodes=1               ### Node count required for the job (usually 1)
#SBATCH --ntasks-per-node=1     ### Nuber of tasks to be launched per Node (usually 1)
#SBATCH --cpus-per-task=40       ### Number of cpus (cores) per task
#SBATCH --mail-user=abbiefayeolson@gmail.com
#SBATCH --mail-type=ALL

conda activate samtools-1.9

/usr/bin/time -v samtools view -buh /projects/bgmp/afo/bi624/deduper/Deduper/Dataset1.sam | samtools sort -@$SLURM_CPUS_PER_TASK > /projects/bgmp/afo/bi624/deduper/Deduper/Dataset1.out.sort.bam
/usr/bin/time -v samtools view -h -o /projects/bgmp/afo/bi624/deduper/Deduper/Dataset1.out.sort.sam /projects/bgmp/afo/bi624/deduper/Deduper/Dataset1.out.sort.bam

/usr/bin/time -v samtools view -buh /projects/bgmp/afo/bi624/deduper/Deduper/Dataset2.sam | samtools sort -@$SLURM_CPUS_PER_TASK > /projects/bgmp/afo/bi624/deduper/Deduper/Dataset2.out.sort.bam
/usr/bin/time -v samtools view -h -o /projects/bgmp/afo/bi624/deduper/Deduper/Dataset2.out.sort.sam /projects/bgmp/afo/bi624/deduper/Deduper/Dataset2.out.sort.bam

/usr/bin/time -v samtools view -buh /projects/bgmp/afo/bi624/deduper/Deduper/Dataset3.sam | samtools sort -@$SLURM_CPUS_PER_TASK > /projects/bgmp/afo/bi624/deduper/Deduper/Dataset3.out.sort.bam
/usr/bin/time -v samtools view -h -o /projects/bgmp/afo/bi624/deduper/Deduper/Dataset3.out.sort.sam /projects/bgmp/afo/bi624/deduper/Deduper/Dataset3.out.sort.bam
