#zweite Schuljahr
#Liste_a4
#Trainingsanalyse
#Im Training wirft jeder Dartspieler 6 Pfeile auf die Dartscheibe
#Es sollen die höchste, niedrigste und durchschnittliche Punktzahl auf der Konsole ausgegeben werden
#Auch Wurfergebnisse über die Konsole eingeben
#Bei einem Wurf sind maximal 60 Punkte erreichbar


import random
import numpy as np

wurf = []
for i in range (0,6):
    x = random.randint(1,60)
    wurf.append(x)
    print("Wurf ",i+1,": ",wurf[i])
 
max = max(wurf)
min = min(wurf)
durchschnitt = np.mean(wurf)
print("bester Wurf: ",max)
print("schlechter wurf: ",min)
print("durchschnittliche Punktzahl: ",durchschnitt)

#Aber diese Aufgabe habe ich leztes Jahr mit for loop gelöst, ohne
#speziele Funktionen zu verwenden
#jetzt habe ich numpy Bibliotheck in Thonny instaliert und viel leichter geworden
#
#nützlich zum gucken
#https://sparkbyexamples.com/numpy/calculate-maximum-numpy-array/



    