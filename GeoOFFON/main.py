#!/usr/bin/env python3

import os
import sys
import csv
from PIL import Image
from PIL.ExifTags import GPSTAGS, TAGS
import time


def create_off(gps_coords):            
    dec_deg_lat = convert_decimal_degrees(float(gps_coords["lat"][0]),  float(gps_coords["lat"][1]), float(gps_coords["lat"][2]), gps_coords["lat_ref"])
    dec_deg_lon = convert_decimal_degrees(float(gps_coords["lon"][0]),  float(gps_coords["lon"][1]), float(gps_coords["lon"][2]), gps_coords["lon_ref"])
    listt=[dec_deg_lat,dec_deg_lon]
    return listt 

def convert_decimal_degrees(degree, minutes, seconds, direction):
    decimal_degrees = degree + minutes / 60 + seconds / 3600

    if direction == "S" or direction == "W":
        decimal_degrees *= -1
    return decimal_degrees
        

print("""

Bonjour, 
Veuillez préparer vos images dans le dossier ./images
Puis saisissez un choix ci dessous 

    Patientez svp !!!                                              
                                                    
""")

time.sleep(5)
os.system("clear")


while True:
    output_choice = int(input("Oû voudriez vous que vos résultats s'affichent :\n\n1 - Fichier text (vous le trouverez dans le dossier results)\n2 - Sur le terminal\nEntrez votre choix ici > "))
    try:
        if output_choice == 1:
            sys.stdout = open("./results/exif_data.txt", "w")
            break
        elif output_choice == 2:
            break
        else:
            print("You entered an incorrect option, please try again.")
    except:
        print("You entered an invalid option, please try again.")


cwd = os.getcwd()
os.chdir(os.path.join(cwd, "images"))
files = os.listdir()
if len(files) == 0:
    print("Vous n'avez aucune image dans le dossier ./images ")
    exit()

with open("../CSV/exif_data.csv", "a", newline="") as csv_file:
    writer = csv.writer(csv_file)
    for file in files:
        try:
            image = Image.open(file)
            print(f"_______________________________________________________________{file}_______________________________________________________________")
            gps_coords = {}
            if image._getexif() == None:
                print(f"{file} ne contient pas de metadata.")
            else:
                for tag, value in image._getexif().items():
                    tag_name = TAGS.get(tag)
                    if tag_name == "GPSInfo":
                        for key, val in value.items():
                            print(f"{GPSTAGS.get(key)} - {val}")
                            if GPSTAGS.get(key) == "GPSLatitude":
                                gps_coords["lat"] = val
                            elif GPSTAGS.get(key) == "GPSLongitude":
                                gps_coords["lon"] = val
                            elif GPSTAGS.get(key) == "GPSLatitudeRef":
                                gps_coords["lat_ref"] = val
                            elif GPSTAGS.get(key) == "GPSLongitudeRef":
                                gps_coords["lon_ref"] = val   
                    else:
                        print(f"{tag_name} - {value}")
                if gps_coords:
                    cords=create_off(gps_coords)
                    dec_deg_lat = cords[0]
                    dec_deg_lon = cords[1]
                    writer.writerow((dec_deg_lat,dec_deg_lon))
                    
        except IOError:
            print("File format not supported!")



sys.stdout=sys.__stdout__


print("""
    
        Voudriez vous géolocaliser les images que vous venez de scanner  ?
        1 - Oui
        * - Non

    
    """)
choice=int(input("Entrez votre choix ici >"))
if (choice==1) :
    while True :
        os.system('clear')

        choice2=int(input("""
        Comment voudriez vous afficher votre résultat ? 
        1 - Offline 
        2 - Online (Pour plus de précision)

        Entrez votre choix ici >"""))
        if choice2 == 2 :
            os.system('python ../map2.py')
            break 
        elif choice2 == 1 :
            os.system('python ../convert.py')
            break

    
        
     

if output_choice == "1":
    sys.stdout.close()
os.chdir(cwd)




