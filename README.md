# THC_meta_abagen
All files from the THC meta analysis using abagen to investrigate CB1R gene expression

File descriptions:

Abagen_main = 'raw' inefficient code 

BOLDcnr1LinearRegression = linear regression model of Hedge's g effect size estimate taken from centroid of 78 brain regions across DK atlas against cbr1 and cnr2 mRNA expression values from allen human brain atlas (from abagen). This is a multiple linear regression using cnr1 and cnr2 as regressors

CB1R_data_analysis = cleaner version of Abagen_main <- reccomend using this over Abagen_main

Dose_egression_code = should be dose_regression_code of course. This is the regression model for THC dose with Hedge's g effect size estimate of brain regions where there was a sig relationship found using SDM (after controlling for route of administration). See data_for_dose_regression.csv for data per brain region (although I may have not uploaded it here to protect the data- will be in external harddrive or on neuroimaging analysis network server at KCL)

MyMean_Hedgesg_effect_extraction_script = this extracts the "MyMean" effect size estimate from .txt files across 78 DK regions. What this means is that it averages the effect size of each study per brain region.

SDM_extraction_code = this makes a mask and extracts the effect size estimate centroid of each brain region for use in regression analyses. This is linked with the MyMean_Hedgesg_effect_extraction_script

csv file named atlas-desikankillany_w_cnr1_7.4.21 contains data for main cannabinoid receptor hedges g analysis- also may not be uploaded here but on NaN server / ext hard drive
