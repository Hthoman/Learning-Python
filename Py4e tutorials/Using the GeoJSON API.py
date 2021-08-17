import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#api key for the DR chuck site 
api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'


address = input('Enter location: ')
parms = dict()
parms['address'] = address
parms['key'] = api_key

url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
        js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)

print(json.dumps(js, indent=4))

lat = js['results'][0]['geometry']['location']['lat']
lng = js['results'][0]['geometry']['location']['lng']
location = js['results'][0]['formatted_address']
place_id = js['results'][0]['place_id']

print('lat', lat, 'lng', lng)
print(location)
print(place_id)
