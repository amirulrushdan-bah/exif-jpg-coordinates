from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import webbrowser
import glob
for filename in glob.glob('*.jpg'):
    print(filename)
    image = Image.open(filename)
    info = image._getexif()
    longitude=[]
    latitude=[]
    coordinate=''
    for tag, value in info.items():
        keys = TAGS.get(tag, tag)
        exif_data = {}
        if(keys=="GPSInfo"):
            #print(str(value))
            for x in value:
                gps_data = {}
                #print(x,value[x])
                if(x==1):
                    latitude.append(value[x])
                    latitude.append(value[x+1])
                if(x==3):
                    longitude.append(value[x])
                    longitude.append(value[x+1])
                if(x==6):
                    altitude=value[x]
    i=0
    print(str(latitude[1]))
    for x in latitude[1]:
        if(x[1]>1):
            coordinate=coordinate+str(x[0]/x[1])
        else:
            coordinate=coordinate+str(int(x[0]/x[1]))
        if (i==0):
            coordinate=coordinate+"°"
        if (i==1):
            coordinate=coordinate+"'"
        i=i+1
    i=0
    coordinate=coordinate+"\""+str(latitude[0])+"+"
    for x in longitude[1]:   
        
        
        if(x[1]>1):
            coordinate=coordinate+str(x[0]/x[1])
        else:
            coordinate=coordinate+str(int(x[0]/x[1]))
        if (i==0):
            coordinate=coordinate+"°"
        if (i==1):
            coordinate=coordinate+"'"
        i=i+1
    coordinate=coordinate+"\""+str(longitude[0])

    print(coordinate)


    webbrowser.open("www.google.com/search?q="+coordinate, new=0, autoraise=True)
