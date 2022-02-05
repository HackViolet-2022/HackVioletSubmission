import googlemaps

line = open('key.txt','r').read()

gmaps = googlemaps.Client(key = line)

gmaps.find_place("woman owned")