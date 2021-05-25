import os


dir_list = os.listdir(r'E:\META_ANALYSIS\THC_analysis\For_extraction')
os.chdir(r'E:\META_ANALYSIS\THC_analysis\For_extraction')


for files in dir_list:
    a = open (files, 'r')
    b = a.readlines()
    c = (b[24], files)
    print (c)






