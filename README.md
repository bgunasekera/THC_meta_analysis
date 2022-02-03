# THC_meta_analysis
abagen = extract mRNA data

dose_regression = THC dose vs Hedge's g effect size estimate of brain regions where there was a sig relationship found using SDM (after controlling for route of administration). 

effect_size_extract_brain_regions = creates ROI mask & extracts the effect size estimate from the centroid of each brain region. Should be ran in cmd terminal

effect_size_extract_pooled = extracts effect size estimate from the txt product of 'effect_size_extract_brain_regions' in a single csv
 
gene_regression = effect size estimate vs abagen data

ggseg_script = plots gene & effect size distributions across the briain 

MRIcroGL_mosaic = creates mosaic of fMRI results
