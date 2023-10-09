#zwei randome zufallzahlen erzeugen
#den nutzer fordern diese zu addieren
#falls richtig, den nutzer loben

import random

falsch = 0
richtig = 0


for i in range(1,10):
    print("addieren Sie die folgende zahlen: ")
    x = random.randint(1,100)
    y = random.randint(1,100)

    print(x,"+",y)
    sum = x + y
    z = float(input("dein Antwort: "))
   
   
    if(z == sum):
        print("prima, dein Antwort ist richtig")
        richtig +=1
        print("-------------nächste Aufgabe-----------------")
    else:
        print("Leider falsch!")
        falsch +=1
        print("-------------nächste Aufgabe-----------------")

print("                         Ende des Herausforderung                    ")
print("                         Richtige Antworten:                         ", richtig)
print("                         Falsche Antworten:                          ",falsch)



