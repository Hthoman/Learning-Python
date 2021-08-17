import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = "http://py4e-data.dr-chuck.net/known_by_Yahya.html" #url to start the script

count=0 #count of how many links followed 
while count < 7:  #loop to follow the links 
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    position=0
    tags = soup('a')
    for tag in tags:  #loop to iterate through the URL until pos 18 is reached 
     position=position+1
     if position==18:
        url=tag.get('href', None)  #pull out link #18 and restart the while loop with +1 count
        count=count+1

print(url)


    