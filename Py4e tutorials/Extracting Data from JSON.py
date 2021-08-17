import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#get the URL and pull it from the website using urllib
url='http://py4e-data.dr-chuck.net/comments_1173727.json'
print('Retrieving', url  )
rawjson=urllib.request.urlopen(url, context=ctx)

#load the json pulled from the site 
data=json.load(rawjson)
#print(json.dumps(data, indent=2))
counter=0
totalcount=[]
for i in data["comments"]:
    currentcount=i['count']
    int(currentcount)
    counter=counter+1
    totalcount.append(currentcount)

print(counter)
print(sum(totalcount))




