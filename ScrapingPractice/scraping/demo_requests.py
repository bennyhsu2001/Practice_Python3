import requests

# url = "https://w3.iiiedu.org.tw/"

# r = requests.get(url)
# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
# print(r.text)

# GET querystring
# url = "https://w3.iiiedu.org.tw/SearchResult.php"
# params = {
#     "classname":"python",
#     "token_2":"aq12ws"
# }
# r = requests.get(url, params=params)
# # print(r.url)
# print(r.text)

#Post Form data
# url = "http://taipei.iiiedu.org.tw/phpro/mod-c.php"
# params = {
#     "qcno":"python"
# }
# r = requests.post(url,data=params)
# if r.status_code == requests.codes.ok:
#     print(r.text)


# headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'}
# url = 'https://tw.yahoo.com/'
# r = requests.get(url, headers = headers)
# print(r.url) 



url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
cookies = {'over18':'1'}
r = requests.get(url,cookies=cookies)
print(r.text)