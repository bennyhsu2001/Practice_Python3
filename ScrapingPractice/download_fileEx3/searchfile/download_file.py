import datetime as dt
import requests
import os
import time


def creat_folder():
    os.makedirs('./five_sec/', exist_ok=True)    
#   creat a forder in local to keep all file. As we creat once, we dont need it anymore.


def date_trans(start1,end1):
    date_int={'year1':int(start1[:4]),'month1':int(start1[4:6]),'day1':int(start1[6:]),'year2':int(end1[:4]),'month2':int(end1[4:6]),'day2':int(end1[6:])}
    
    start_date = dt.datetime(date_int['year1'],date_int['month1'],date_int['day1'])
    end_date = dt.datetime(date_int['year2'],date_int['month2'],date_int['day2'])
    totaldays = (end_date - start_date).days + 1
    return start_date,totaldays


def download_file(start_date,totaldays):
    for daynumber in range(totaldays):
        date1=(start_date + dt.timedelta(days = daynumber)).date()
        datestring = date1.time.strftime('%Y%m%d')    #.replace('-', '') 

        five_sec_url='http://www.tse.com.tw/exchangeReport/MI_5MINS_INDEX?response=csv&date=%s'%datestring
        r = requests.get(five_sec_url)
        
        lst = split_content(r)
        tup = [parser(i) for i in lst[-10].split(',')]
        print(tup)
        
#         if date1.weekday() < 5:
#             with open('./five_sec/%s.csv'@datestring,'wb')as f:
#                 f.write(r.content)
#     return r


def parser(s):
    s = s.strip('""').replace(",", "")
    if ":" not in s and len(s)>0:
        s = float(s)
    return s


def split_content(r):
    s = str(r.content)
    lst = s.split("\\r\\n")
    return lst


# main
# creat_file()
t1 = time.time()  # record start time
map(download_file,date_trans('20180810','20180811'))
print('Total time:',time.time()-t1)    # count total time


