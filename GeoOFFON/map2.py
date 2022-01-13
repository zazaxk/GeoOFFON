#!/usr/bin/env python3

import folium
import csv
from csv import reader
import os 
from folium.features import CustomIcon







m = folium.Map(location=[28.02898, 1.66667],zoom_start=5)






path='../all.geojson'
folium.GeoJson(path, name="geojson").add_to(m)
points=[]

with open('../CSV/exif_data.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        
        folium.Marker(
        row
        ).add_to(m)
        points.append([float(row[0]),float(row[1])])
#points.append(points[0])
print('\nRecupertaion de données avec succès')
first=points[0]
points.append(first)
print('Veuillez patienter un moment svp')
folium.PolyLine(points,color='red').add_to(m)



m.save("../index.html")

os.system('firefox ../index.html')
