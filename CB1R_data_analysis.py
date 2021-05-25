import abagen
import pandas as pd
import nibabel as nib

files = abagen.fetch_microarray(donors='all', data_dir=r'E:\abagen-data')
atlas = abagen.fetch_desikan_killiany() # CHECK IF YOU WANT IMAGES IN NATIVE SPACE OR NOT- SECTION 2.3


# WITHIN REGIONS OF AN ATLAS
expression = abagen.get_expression_data(atlas['image'], atlas['info'], probe_selection='diff_stability', donor_probes='aggregate', gene_norm='scaled_robust_sigmoid', region_agg='donors', agg_metric='mean')
print(expression)

genes = (
    expression ['CNR1'],
    expression ['CNR2'],
    expression ['FAAH'],
    expression ['MGLL'],
    expression ['BDNF'])
print (genes)

df = pd.DataFrame(genes)
df.to_csv('genes.csv')

#https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0037714
#For BDNF gene: "more variably expressed in childhood"

#BELOW IS FOR SUBSEQUENT OPTIONAL ANALYSIS -- NOT FOR MY META ANALYSIS
#SECTION 8 -- USING A BINARY MASK


#print ('---------BINARY MASK----------')
#dk = nib.load(atlas['image'])
#phg = dk.__class__(dk.dataobj[:] == 67, dk.affine, dk.header) #CHANGE NUMBER TO LABEL BASED ON ATLAS IN .CSV FILE

#expression, coords = abagen.get_samples_in_mask(mask=phg)  #CHANGE TO (mask=None) IF WANT ALL SAMPLES IN NO MASK
#print (expression)
#print (expression ['CNR1'])





# ---- NOTES ON OUTPUT ---
# Values are microarray expression data normalized and aggregated across donors
# Expression values for a given gene will range from 0-1.
# 0= region with the lowest expression of that gene
# 1 indicates the region with highest.

# Rows correspond to region labels as defined in the atlas image (FOR ATLAS ONLY)
# In binary mask, the returned expression dataframe is a samples x gene matrix (rather than regions x gene),
# Therefore, the index of the dataframe corresponds to the unique well ID of the relevant sample
# (rather than the atlas region) -- SEE SECTION 8.1 FOR MORE INFORMATION




