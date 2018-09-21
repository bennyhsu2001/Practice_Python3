import urllib.request as UR
import xml.etree.ElementTree as ET

url = 'https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=36847f3f-deff-4183-a5bb-800737591de5&format=xml'
with UR.urlopen(url) as res:
    datas = res.read().decode('utf-8')
    tree = ET.fromstring(datas)  
    # print(tree.tag)   # data > root element
    for child in tree:
        print('{} - {}'.format(child.find('CAT2').text,child.find('stitle').text))
       
