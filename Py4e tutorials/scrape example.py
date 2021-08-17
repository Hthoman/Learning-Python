from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl
# check if the string contains a valid url
# return a Dict() of fulllongURL & host if True
# return False if False
def checkURL(chk):
    # regex source:
    # https://mathiasbynens.be/demo/url-regex (I copied this one, and made some small changes)
    # https://gist.github.com/dperini/729294
    # https://regex101.com/r/WDetqc/1 (helped me to analysis the regex & placing down ?P)
    p = re.compile(r"(?P^(?:(?:https?|ftp)://)(?P(?:\S+(?::\S*)?@)?(?:(?!10(?:\.\d{1,3}){3})(?!127(?:\.\d{1,3}){3})(?!169\.254(?:\.\d{1,3}){2})(?!192\.168(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})))(?::\d{2,5})?)(?:/[^\s]*)?$)", re.MULTILINE&re.IGNORECASE)
    if p.match(chk) != None: return p.match(chk).groupdict()
    else: return False

# Read then Decode the data bytes received w/ BS4
def blyat(link):
    html = urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Check Valid URL input
while True:
    url = checkURL(input('Enter URL: '))
    url = checkURL('http://py4e-data.dr-chuck.net/known_by_Rachael.html').get('fullURL')
    if not url: print('input a valid URL')
    else: break

# Checking everything lol
try: count = int(input('Enter count:'))
except: print('Enter correct Number')
try: pos = int(input('Enter position:'))
except: print('Enter correct Number')

# find & print the link (iykwim)
soup = blyat(url)
for x in range(count):
    tags = soup.find_all('a', limit=pos)[pos-1].get('href')
    print(tags)
    soup = blyat(tags)