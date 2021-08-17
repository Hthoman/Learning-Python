import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('enter url to be extracted')
print('retrieving', url)

rawdata=urllib.request.urlopen(url, context=ctx)

data=rawdata.read()
print('retrived', len(data), 'characters' )

tree=ET.fromstring(data)
count=0
elementlst=[]
for elements in tree.findall(".//count"):
    rawelem=elements.text
    intelem=int(rawelem)
    elementlst.append(intelem)
    count=count+1





print(count)
print(sum(elementlst))
