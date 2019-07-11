#!/bin/bash
  
dsub \
    --provider google-v2 \
    --project encode-uk-biobank \
    --zones "us-east1-b" \
    --logging gs://ran/log/loo-no-MAFLD-ypred/ \
    --disk-size 100 \
    --machine-type n1-highmem-8 \
    --image "gcr.io/encode-uk-biobank/fi-priors" \
    --script "compute_ypred_noconf_BLDv2.2.py" \
    --tasks "submit_list1.tsv"
