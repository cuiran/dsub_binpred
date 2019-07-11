#!/usr/bin/env python
  
import subprocess
import os

ANNOT_PREFIX = os.environ['ANNOT_PREFIX']
CHR = os.environ['CHR']
COEF_DIR = os.environ['COEF_DIR']
OUT_DIR = os.environ['OUT_DIR']

# make directories
subprocess.call(['mkdir','/mnt/data/annot/'])
subprocess.call(['mkdir','/mnt/data/coef/'])
subprocess.call(['mkdir','/mnt/data/results/'])
subprocess.call(['mkdir','/mnt/data/results/no-MAFLD/'])
# copy data
subprocess.call(['gsutil','-m','cp','gs://ran/functionally_informed_fm/data/baselineLF_v2.2_allsnps_UKBB/baselineLD/baselineLD_withID.'+CHR+'.annot.gz','/mnt/data/annot/'])
subprocess.call(['gsutil','-m','cp','gs://ran/functionally_informed_fm/results/binned_prediction/UKBB.T2D.susie/leave-one-out/*BLDv2.2.avebinpred_bin'+CHR+'_*.coef','/mnt/data/coef/'])
subprocess.call(['gsutil','-m','cp','gs://ran/functionally_informed_fm/results/binned_prediction/UKBB.T2D.susie/leave-one-out/*BLDv2.2.avebinpred*pred'+CHR+'.coef','/mnt/data/coef/'])


# run script
subprocess.call(['python','/home/pyscripts/remove_confound.py',
    '--compute-ypred',
    '--annot-prefix', ANNOT_PREFIX,
    '--chrom', CHR,
    '--coef-dir', COEF_DIR,
    '--BLD',
    '--result-dir', OUT_DIR])

subprocess.call(['gsutil','-m','cp',OUT_DIR+'*','gs://ran/functionally_informed_fm/results/binned_prediction/UKBB.T2D.susie/loo-no-MAFLD/'])
