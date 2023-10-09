#zwei randome zufallzahlen erzeugen
#den nutzer fordern diese zu addieren
#falls richtig, den nutzer loben
#wiederholen 10 Mal
#Am Ende geben wie viel falsch und wie viel richtige Antworten gab

import random

falsch = 0
richtig = 0

print("Herausforderung randome zahlen addieren: ")

for i in range(1,11):
    
    x = random.randint(1,100)
    y = random.randint(1,100)
    sum = x + y
    print("Aufgabe",i,":     ", x,"+",y)
    z = int(input(" = "))
    

   
    
    
   
   
    if(z == sum):
        print("prima!")
        print("                           ")
        richtig +=1
        
    else:
        print("Leider falsch! richtig wäre ",z)
        falsch +=1
        

print("                         Ende des Herausforderung  ")
print("                         Richtige Antworten:        ", richtig)
print("                         Falsche Antworten:         ",falsch)



