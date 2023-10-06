#zweite Schuhljahr
#Liste_a3
#Gewinnziehung

#Am Abend des Dart-Events findet die Ziehung der Gewinnerlose statt. Der Ziehungsleiter soll die Möglichkeit
#erhalten, die gezogenen Losnummern in einem Array zu speichern.
#Nachdem die fünf Losnummern mit Gewinnen gezogen worden sind, sollen sie ausgegeben werden.


#Erste Variante auch in leztes jahr gelöst


import random
los = [] # ein lear array für Gewinnlotterie initialisieren


for i in range(0,4):
    num = random.randint(1000,9999)
    los.append(num)
    print("Gezogene losnummer: ",los[i])
    
print("--------------Gewinnlose---------------------")
for i in range(0,len(los)):
    print(los[i])

       
#zweite variante wenn man von konsol die Zahlen angibt
"""los = []
for i in range(0,5):
    print("Gewinnlose eingeben: ")
    num=int(input())
    los.append(num)
print("Gewinnlose",los)"""
    

    

