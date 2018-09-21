import urllib.parse as UP
import urllib.request as UR

url = "https://24h.pchome.com.tw/prod/DGAD8T-A9008GS42?fq=/S/DGADA9#k1"
o = UP.urlparse(url)
print(o)
print(o.scheme)
print(o.query)
print(o.path)
o = o._replace(path='prod/DGAD01-A900689OG')
print(UP.urlunparse(o))
#  

data = UP.quote("中文")
print(data)
data = UP.unquote(data)
print(data)


url = "http://taipei.iiiedu.org.tw/"
with UR.urlopen(url) as response:
    print(response.read().decode('utf8'))

