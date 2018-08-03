'''
Created on 2018年7月31日

@author: Student
'''
import csv
with open('secret/EF05M01.csv','r',encoding='\ufeff') as testData:
#encoding should be'\ufeff'. if it is "utf-8", then the [0][0] item will have \ufeff problem
    dat=[k for k in csv.reader(testData)]
    for line in dat:
        print (line);
print(type(dat[0][0]));
# all the data in array will be str
# if u use csv package import data, it will be just 2 dimantion.
with open('secret/out.csv','w',newline='') as setData:
    writer=csv.writer(setData)
    writer.writerows(dat)
    

    