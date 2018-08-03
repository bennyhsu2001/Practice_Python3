'''
Created on 2018年7月31日

@author: Student
'''
import numpy as np
import csv 

dat = np.loadtxt('secret/EF05M01.csv',delimiter=',',skiprows=1, dtype=float)

np.savetxt('secret/NPcsv.csv',dat,fmt='%s %d %d %d',
            header='id,A1,A2,A3', commemts='')
