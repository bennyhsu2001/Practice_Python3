import requests
import time
# url = "https://www.ptt.cc/bbs/Gossiping/index.html"
# r = requests.get(url, cookies={"over18":"1"})
# print(r.text)

url = "https://tw.yahoo.com/"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
mobil_headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}

time.sleep(2)
r = requests.get(url,headers=mobil_headers)
print(r.url)