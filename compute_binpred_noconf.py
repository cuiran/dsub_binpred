#!/usr/bin/env python

import subprocess
import os

CHR = os.environ['CHR']
PIP_FILE = os.environ['PIP_FILE']
NUM_BINS = os.environ['NUM_BINS']
YPRED_DIR = os.environ['YPRED_DIR']

# make directories
subprocess.call(['mkdir','/mnt/data/pip/'])
subprocess.call(['mkdir','/mnt/data/ypred/'])

# copy data
subprocess.call(['gsutil','-m','cp','gs://ran/functionally_informed_fm/results/UKBB_T2D_finemapped_flat/UKB.T2D.SAIGE.all.snp','/mnt/data/pip/'])
subprocess.call(['gsutil','-m','cp','gs://ran/functionally_informed_fm/results/binned_prediction/UKBB.T2D.susie/loo-no-MAFLD/*pred'+CHR+'.*.ypred','/mnt/data/ypred/'])

# run script
subprocess.call(['python','/home/pyscripts/remove_confound.py',
    '--compute-binpred',
    '--chrom',CHR,
    '--pip-file',PIP_FILE,
    '--num-bins',NUM_BINS,
    '--ypred-dir',YPRED_DIR])

# copy data to bucket
subprocess.call(['gsutil','-m','cp','/mnt/data/ypred/*'+str(NUM_BINS)+'bins*','gs://ran/functionally_informed_fm/results/binned_prediction/UKBB.T2D.susie/loo-no-MAFLD/'])
