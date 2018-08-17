# get fields and sav to csv file
import csv

# source csv file
sname='/vagrant/performance_detail.csv'

# target csv file
tname='/vagrant/flightdata.csv'

nr=0    # number of records

with open(sname,'r') as sf, open(tname,'w') as tf:
    reader=csv.reader(sf)
    writer=csv.writer(tf)
    
    for row in reader:
        data=row[:29]
        writer.writerow(data)
        nr+=1
        not nr%100000 and print('.',end=' ',flush=True)

    print('\n')