import urllib.request as ur
import json
url = "https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=24c9f8fe-88db-4a6e-895c-498fbc94df94"

with ur.urlopen(url) as data:
    obj = json.loads(data.read().decode('utf-8'))
    for i in obj['result']['results']:
        print(i["o_tlc_agency_name"])



