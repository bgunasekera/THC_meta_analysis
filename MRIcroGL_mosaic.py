import gl

gl.resetdefaults()
gl.loadimage('mni152') #This is the T1 template
gl.overlayload('E:\META_ANALYSIS\THC_analysis\Analysis_17_02_20\MyMean_z_p_0.00500_1.000_10.nii') #Change to overlay of interest
gl.overlayload('E:\META_ANALYSIS\THC_analysis\Analysis_17_02_20\MyMean_z_p_0.00500_1.000_10_neg.nii') #Use two if want to overlay two maps ontop of one another
gl.minmax(1, 0, 3) #Min and max thresholding for each image
gl.minmax(2, 0, 3)
gl.backcolor (250,250,250)
gl.colorname (1,"Inferno") #Colour palette
gl.colorname (2,"electric_blue")
gl.linecolor (0,0,0)
gl.linewidth(1)
gl.colorbarsize (0.025)
gl.colorbarposition (2)
gl.mosaic('A H -0.1 V -0.1 -48 -16 -3; -0.1 13 19; 41 55 S X R 0') #Slices- uses y coordinate