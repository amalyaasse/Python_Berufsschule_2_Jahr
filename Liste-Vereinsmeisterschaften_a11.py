#Zweite Schuljahr
#Algorithmen
#liste_a1

name=["Matthias Schmitt","Felix Holzman","Sabrina Eggers","Sebastian Wolf","Niklas Eisenbaum"]
print("Welche Platzierung soll ausgegeben werden?: ")
x = int(input())
for i in range(len(name)):
    if i==x:
        myAusgabe ="Platzierung {} : "
        print(myAusgabe.format(x)+name[i-1]) #format(x) bedeutet statt {} wert von x stellen
        break
    elif x<i or x>len(name):
        print("Diese Platz existiert nicht")
        break


#Use the format() method to insert numbers into strings:
    
teilnahmerzahl = "Teilnahmerzahl: {}"
y=len(name)
print(teilnahmerzahl.format(y))


    
            
    
      