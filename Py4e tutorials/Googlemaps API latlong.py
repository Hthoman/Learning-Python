import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Enter a valid google places API key
api_key =input('Enter Google places API key')
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

#enter and set parameters for geocoded location
address = input('Enter location: ')
parms = dict()
parms['address'] = address
parms['key'] = api_key
#encode parameters 
url = serviceurl + urllib.parse.urlencode(parms)

#update user on request for geocoded location
print('Fetching', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Fetched', len(data), 'characters')

#check to see if google places sent the geojson
try:
    js = json.loads(data)
except:
        js = None
#failure messgage if geojson not sent
if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)
    #check if valid API was used 
    googlecheck='The provided API key is invalid'
    if googlecheck in data:
        print("chere here to obtian an API key https://developers.google.com/maps/documentation/places/web-service/get-api-key")
    quit()

#print full geojson for user 
print(json.dumps(js, indent=4))

#define lat/long
lat = js['results'][0]['geometry']['location']['lat']
lng = js['results'][0]['geometry']['location']['lng']
location = js['results'][0]['formatted_address']
place_id = js['results'][0]['place_id']

#print Lat/long, location, and google places id
print('lat', lat, 'lng', lng)
print(location)
print(place_id)
