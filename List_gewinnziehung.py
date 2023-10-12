#Liste_a3
#Gewinnlotterie
#man muss ein los kaufen
#es findet die Ziehung der Gewinnerlose statt
#Die gezogenen Losnummern in einer Liste speichern

#print("Gezogene Losnummer:")
import random
los =[]

#erste Variante
"""for i in range (1,6):
    print("Gewinnlose eingeben:")
    x=int(input())
    los.append(x)
    i=+1
print("Gozogene Losnummern sind:",los)"""


#zweite Variante

for i in range (1,6):
    x=random.randint(1000,9999)
    print("Gezogene Losnummer:",x)
    los.append(x)
    i=+1
print("----------Gewinnlose------------------")
for i in range(0,len(los)):
    print(los[i])
    i=+1
    
    
        


