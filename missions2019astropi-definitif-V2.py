# MISSION 2019 : détection du champ magnétique en fonction du jour/nuit
# Ecole de Saint-André d'Embrun, Hautes-Alpes, France
# CM1 et CM2
# 2019 MISSION : magnetic field detection in fonction of day/night
# Saint-André d'Embrun Primary School, Hautes-Alpes, France
# Year 5 and Year 6
# Equipe des Robotiseurs
# Robotiseurs Team

# import du module SenseHat
# SenseHat module import
from sense_hat import SenseHat
sense = SenseHat()

# import du module camera
# Camera module import
from picamera import PiCamera
cam = PiCamera()

# import du module time
# time module import
import time
import datetime
from time import sleep


# import os
# os import
import os

# configuration du chemin pour les photos
# path configuration for photos
dossier = os.path.dirname(os.path.realpath(__file__))

# définition des couleurs pour l'affichage Leds du Sense Hat
# color definition for Leds Sense Hat
g = (0, 255, 0)
r = (255, 0, 0)
u = (0, 0, 255)
y = (255, 255, 0)
o = (237, 127, 16)
b = (0, 0, 0)
w = (255, 255, 255)
v = (102, 0, 153)
p = (253, 108, 158)
s = (96, 96, 96)
n = (91, 60, 17)

# image Sense Hat signalant la capture du champ magnétique
# Sense Hat picture when reading magnetic field data 
aimant = [w, w, b, w, w, b, w, w,
          w, w, w, b, w, w, w, w,
          w, b, b, w, w, b, b, w,
          w, r, r, w, w, r, r, w,
          w, r, r, w, w, r, r, w,
          w, r, r, w, w, r, r, w,
          w, r, r, r, r, r, r, w,
          w, r, r, r, r, r, r, w,]
          

# image Sense Hat signalant la Terre unr fois un cycle effectué de données
# Sense hat Earth picture when one loop done
terre = [b, b, u, u, u, u, b, b,
         b, u, g, g, u, u, u, b,
         u, u, g, g, g, u, u, u,
         u, u, g, u, u, u, g, u,
         u, u, g, g, u, g, g, u,
         u, u, u, g, u, u, g, u,
         b, u, u, u, u, u, u, b,
         b, b, u, u, u, u, b, b,]

# image Sense Hat signalant l'appareil photo 1
# Sense Hat picture animation when photo IR is saved

photo1 = [w, w, w, w, w, w, w, w,
         w, w, w, w, w, w, r, w,
         w, b, b, b, b, b, b, w,
         w, b, u, u, b, u, b, w,
         w, b, u, u, b, b, b, w, 
         w, b, b, b, b, b, b, b,
         w, b, b, b, b, b, b, b,
         w, w, w, w, w, w, w, w,]

# image Sense Hat signalant l`appareil photo 2
# Sense hat picture animation when photo IR is saved
photo2 = [w, w, w, w, w, w, w, w,
          w, w, w, w, w, w, w, w,
          w, b, b, b, b, b, b, w,
          w, b, y, y, b, u, b, w,
          w, b, y, y, b, b, b, w,
          w, b, b, b, b, b, b, w,
          w, b, b, b, b, b, b, w,
          w, w, w, w, w, w, w, w,]

# effacer leds Sense Hat
# Clear Sense Hat Leds
sense.clear()

# ouverture d'un fichier nommé champ magnétique pour ajouter les données x, y, z
# open file fichier1 to save x,y,z magnetic filed data nanoTesla
fichier1 = open("champmagnetique.csv", "a")

# pour écrire dans le fichier le nom des colonnes
# to write in file fichier1 columns'names
fichier1.write("Date, champmagnetique x y z \n")

# programme de stockage du temps
# time saved
now_time = datetime.datetime.now()

# heure de départ du test
# departure time of program
timedepart = time.time()

# durée du test en secondes
# program duration - seconds 
# timesortie = 60*2 #pour nos tests sur deux minutes for our 2 minutes'test
# timesortie de 178 min pour l'ISS End duration for program in ISS
timesortie = 60*178

# mise à 0 du compteur de photos utilisé uniquement pour les tests dans le shell
# photo counter to 0  shell display only for test
# numero_photo = 0

# répéter jusqu'à ce qu'on atteigne 178 min de test
# repeat until 178 minutes
while time.time() < timedepart + timesortie:

    # Prise de photo avec date
    # photo taken with time stamp          
        temps = time.asctime( time.localtime(time.time()) )
        print(temps)
        cam.capture(dossier+"/image_"+ str(temps)+".jpg")
        # incrementation du compteur de photo uniquement pour les tests dans le shell
        # photo counter incrementation only when we test in shell 
        # numero_photo+=1
        # affichage dans le shell du numéro de la photo uniquement lors des tests
        # display photo number into the shell when we test
        # print(numero_photo)
        
        #affichages  animation Leds sur le Sense Hat de l'image photo + 1 seconde
        #display Sense hat Leds animation when photo is taken
        sense.set_pixels(photo1)
        sleep(2)
        sense.set_pixels(photo2)
        sleep(2)

        # relevé du capteur champ magnétique en nanoTesla
        # magnetic field data reading    
        magnetique = sense.get_compass_raw()
        x = magnetique['x']
        y = magnetique['y']
        z = magnetique['z']

        # arrondi à 4 décimales
        # 4 decimal round    
        x=round(x, 4)
        y=round(y, 4)
        z=round(z, 4)

        # affichage dans le shell
        # magnetic field data displaying into shell    
        print("x={0}, y={1}, z={2}".format(x, y, z))

        # affichage Leds sur le Sense Hat de l'image de l'aimant
        # display Sense Hat Leds - Magnet picture    
        sense.set_pixels(aimant)
        sleep(1)

        # écrire les données générales dans le fichier champ magnétique
        # write magnetic field data into file fichier1    
        fichier1.write(time.strftime('%d %m %y %T'))
        fichier1.write(",")
        fichier1.write(str(magnetique))
        fichier1.write("\n")

        # affichage Leds sur le Sense Hat du champ magnetique sur les 3 axes
        # diplay Sense Hat Leds magnetic field data    
        sense.show_message("x:{0}, y:{1}, z:{2}".format(x, y, z), text_colour = g, scroll_speed=0.03)

        # affichage Leds sur le Sense Hat de l'image Terre
        # display Sense Hat Leds - Earth    
        sense.set_pixels(terre)
        # attente de 25 secondes pour avoir 2 relevés de données et 2 photos par minute
        # waiting for 25 seconds to obtain 2 data records and 2 photos by minute
        sleep(25)

# fermeture du fichier des données champ magnétique
# close magnetic field data file fichier1    
fichier1.close()
            
