import urllib.request
import json
import csv

loc = []
with open('location.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        loc.append(row['location'])

print(loc)
orig_coord = '22.9872,120.2114'
dest_coord = '22.98624,120.21703'
url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&&sensor=false".format(str(orig_coord),str(dest_coord))
result = json.load(urllib.request.urlopen(url))
dis = result['rows'][0]['elements'][0]['distance']['value']
# print(json.dumps(result, indent=4, sort_keys=True))
print(dis)
