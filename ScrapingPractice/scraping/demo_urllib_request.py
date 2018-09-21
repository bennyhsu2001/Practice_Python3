import urllib.request as UR
import urllib.parse as UP
# url = "https://w3.iiiedu.org.tw/"
# with UR.urlopen(url) as f:
#     print(f.read().decode('big5'))
url = "https://w3.iiiedu.org.tw/SearchResult.php"

# ?classname=python&token_2=aq12ws
params = {
    "classname":"python",
    "token_2":"aq12ws"
}
query_string = UP.urlencode(params)
o = UP.urlparse(url)
o = o._replace(query=query_string)
url = UP.urlunparse(o)
# print(url)
with UR.urlopen(url) as f:
    # print(f.read().decode('big5'))
    file_obj = open('iiiedu.html','w',encoding="utf-8")
    file_obj.write(f.read().decode('big5'))
    file_obj.close()