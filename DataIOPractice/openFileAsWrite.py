'''
Created on 2018年7月31日

@author: Student
'''
ApplePen=['Apple','Pen']
with open('secret/ApplePen.txt','w',encoding="utf-8") as PPAP:
    PPAP.write('This is an apple.\nThis is a pen.\n');
    PPAP.writelines(ApplePen)
# if u do this shit twice the second time will cover the first vision.

    