import googlemaps
import requests


line = open('key.txt','r').read()

gmaps = googlemaps.Client(key = line)

