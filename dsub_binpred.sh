#!/bin/bash
  
dsub \
    --provider google-v2 \
    --project encode-uk-biobank \
    --zones "us-east1-b" \
    --logging gs://ran/log/loo-no-MAFLD-binpred/ \
    --disk-size 100 \
    --machine-type n1-highmem-4 \
    --image "gcr.io/encode-uk-biobank/fi-priors" \
    --script "compute_binpred_noconf.py" \
    --tasks "submit_list_binpred.tsv"
