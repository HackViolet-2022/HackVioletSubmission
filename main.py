import googlemaps

with open('key.txt') as f:
    line = f.readline()

f.close()
gmaps = googlemaps.Client(key = line)

