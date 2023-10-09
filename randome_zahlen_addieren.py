#zwei randome zufallzahlen erzeugen
#den nutzer fordern diese zu addieren
#falls richtig, den nutzer loben

import random

print("addieren Sie die folgende zahlen: ")
x = random.randint(1,100)
y = random.randint(1,100)

print(x,"+",y)
sum = x + y
z = float(input("dein Antwort: "))

if(z == sum):
    print("prima, dein Antwort ist richtig")
else:
    print("Leider falsch!")


