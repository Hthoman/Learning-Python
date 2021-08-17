import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

count=0
commentlst=[]

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1173724.html"
html = urlopen(url, context=ctx).read()
#html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all SPAN tags
tags = soup('span')
for tag in tags:
    # record the number of comments and sum their value
    count=count+1
    commentvalue=int(tag.contents[0])
    commentlst.append(commentvalue)
    

print(count)
print(sum(commentlst))

    
   