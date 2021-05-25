#SECTION 1.1
import abagen


files = abagen.fetch_microarray(donors='all', verbose=0)

#SECTION 1.2
print(files.keys())
print(sorted(files['9861']))

data = files['9861']
annotation = abagen.io.read_annotation(data['annotation'])
print(annotation)

probes = abagen.io.read_probes(data['probes'])
print(probes)

#SECTION 2.1
atlas = abagen.fetch_desikan_killiany()

print(atlas['image'])
print(atlas['info'])

#SECTION 2.2 -
import pandas as pd
atlas_info = pd.read_csv(atlas['info'])
print(atlas_info)

from abagen import utils
utils.check_atlas_info(atlas['image'], atlas['info'], validate=True)

#SECTION 2.3
atlas = abagen.fetch_desikan_killiany(native=True)
print(atlas['image'].keys())
print(atlas['image']['9861'])

#SECTION 3.1 -- IF STRUGGLING TO GET RESULTS REVIEW THIS SECTION
pd.read_csv(atlas['info'])
expression = abagen.get_expression_data(atlas['image'], atlas['info'])
print(expression)

#SECTION 4.1.5 -- CHOICE WAS RECCOMENDED -- REVIEW WITH SAGNIK
abagen.get_expression_data(atlas['image'], probe_selection='diff_stability')

#SECTION 5.1 -- CHOICE WAS RECCOMENDED -- REVIEW WITH SAGNIK
abagen.get_expression_data(atlas['image'], donor_probes='aggregate')

#SECTION 6.2.8 CHOICE WAS RECCOMENDED -- REVIEW WITH SAGNIK -- FOR 1) METHOD AND 2) SAMPLE-VS-GENE_NORM
abagen.get_expression_data(atlas['image'], gene_norm='scaled_robust_sigmoid')

#SECTION 8.1 -- OBTAIN MICROARRAY SAMPLES WITHIN MASK
import nibabel as nib
atlas = abagen.fetch_desikan_killiany()
dk = nib.load(atlas['image'])
phg = dk.__class__(dk.dataobj[:] == 67, dk.affine, dk.header) #CHANGE NUMBER TO LABEL BASED ON ATLAS IN .CSV FILE

print ('---------EXPRESSION CAT IN HAT----------')
expression, coords = abagen.get_samples_in_mask(mask=phg)  #CHANGE TO (mask=None) IF WANT ALL SAMPLES IN NO MASK
print (expression)
print (expression['A1BG'])
print (expression ['CNR1'])





