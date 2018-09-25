import requests
import time
from bs4 import BeautifulSoup

url = "https://www.taifex.com.tw/chinese/3/7_12_3.asp"

headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
post_data={
    'goday':'', 
    'DATA_DATE_Y': '2018',
    'DATA_DATE_M': '9',
    'DATA_DATE_D': '21',
    'syear': '2018',
    'smonth': '9',
    'sday': '21',
    'datestart': '2018/9/21',     #這個參數以上表示的是日期應該可以了解
    'COMMODITY_ID': ''         #這個部分就是網頁契約的部分 TXF表示臺股期貨、EXF表示電子期貨.....，空字串''表示全部
}


time.sleep(2)
response = requests.post(url,headers=headers,data=post_data)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "lxml")

#搜尋期貨契約表格下的一列列tr資料
rows = soup.select('table.table_f tr')

#下面這段參考看看，我嘗試說明如下
#每個商品名稱都有三個身分別，自營商、投信、外資
#每一個身分別都是一個tr，所以一個商品有三個tr   我用i來計算三個tr屬於同一個商品
#第一個tr的第一個及第二個td都有rowspan="3"這個屬性
#這表示每個商品的第二及第三個tr都比第一個tr少兩個td
#所以我用i==1判斷是第一個tr，還是其它tr
#另外contents會將空白or\n也當成是一筆資料所以contents[0]得到的是空字串
#因此第一個td是contents[1]，第二個td是contents[3]，......依序下去
i=0
for row in rows:    
    i += 1
    if i == 1:
        cell1 = row.contents[1].string   
        if cell1 and cell1.isdigit():
            print("{}-{}".format(cell1,row.contents[3].get_text()))
            print(row.contents[5].get_text(),row.contents[7].get_text())
    else:
        print(row.contents[1].get_text(),row.contents[3].get_text())

    if i == 3:
        print("--------------------------")
        i = 0