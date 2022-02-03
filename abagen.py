import abagen
import pandas as pd


files = abagen.fetch_microarray(donors='all', data_dir=r'E:\abagen-data')
atlas = abagen.fetch_desikan_killiany() 

#%%
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


