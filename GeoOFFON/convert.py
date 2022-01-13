import csv
from csv import *
from tkinter import *
from PIL import *
def conv_lat(row):
    row=float(row)
    lat=36.967227-row
    lat=(lat*472)/23.138497
    return int(lat)
def conv_long(row):
    row=float(row)
    longg=row+8.825079
    longg=(longg*519)/22.653809
    return int(longg)

canvas = Canvas(width = 519, height = 472, bg = 'blue')
canvas.pack(expand = YES, fill = BOTH)

image = PhotoImage(file = "../alg/algg.png")
mr = PhotoImage(file = "../alg/mr.png")
canvas.create_image(0, 0, image = image, anchor = NW)




lat=[]
longg=[]
with open('../CSV/exif_data.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        if row  :
            print(row)

            lat.append(conv_lat(row[0]))
            longg.append(conv_long(row[1]))
            print(conv_lat(row[0]))
            print(conv_long(row[1]))
            canvas.create_image(conv_long(row[1]), conv_lat(row[0]), image = mr, anchor = NW)
for i in range (0,len(lat)) :
    canvas.create_line(longg[i-1]+12,lat[i-1]+12,longg[i]+12,lat[i]+12,fill="black",width=2)
mainloop()
        