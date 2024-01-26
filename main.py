# Dependencies
import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

#Her er lenken til den grati API
VarUrl = "http://api.open-notify.org/astros.json"

# Her åpner den URL med å bruke request modulen.
VarResponse = urllib.request.urlopen(VarUrl)

#Denne koden her åpner json filen og leser den.
VarResult = json.loads(VarResponse.read())

#Denne åpner txt filen.
VarFile = open("iss.txt", "w")
VarFile.write("There are currently " +
           str(VarResult["number"]) + " astronauts on the ISS: \n\n")
VarPeople = VarResult["people"]
for p in VarPeople:
    VarFile.write(p['name'] + " - on board" + "\n")

# Her blir long og lat printet ut fra informasjonen som er hentet av API fra NAS
g = geocoder.ip('me')
VarFile.write("\nYour current lat / long is: " + str(g.latlng))
VarFile.close()
webbrowser.open("iss.txt")

# Dette er for å kunne sette opp verdens kartet i turtle modulen, som de forskjellige kordinatene.
VarScreen = turtle.Screen()
VarScreen.setup(1280, 720)
VarScreen.setworldcoordinates(-180, -90, 180, 90)

# Dette er for og laste inn verdenskartet eller få den til og starte:
VarScreen.bgpic("map.gif")
VarScreen.register_shape("iss.gif")
VarIss = turtle.Turtle()
VarIss.shape("iss.gif")
VarIss.setheading(45)
VarIss.penup()

while True:
    # Denne koden her henter informasjon fra API lenken og laster ned status av ISS stasjonen i virkelig tid.
    VarUrl = "http://api.open-notify.org/iss-now.json"
    VarResponse = urllib.request.urlopen(VarUrl)
    VarResult = json.loads(VarResponse.read())

    # Ekstrakt ISS Lokasjonen.
    VarLocation = VarResult["iss_position"]
    VarLat = VarLocation['latitude']
    VarLon = VarLocation['longitude']

    # Ouput lon og lat til Terminalen.
    VarLat = float(VarLat)
    VarLon = float(VarLon)
    print("\nLatitude: " + str(VarLat))
    print("\nLongitude: " + str(VarLon))

    # Her Opptadetere ISS stasjonen sin lokasjon på kartet.
    VarIss.goto(VarLon, VarLat)

    # Denne gjør sånn at bilde av ISS stasjonen og kartet refresher seg hver 5 sekund, slik at man kan se endringen fysisk.
    time.sleep(5)
