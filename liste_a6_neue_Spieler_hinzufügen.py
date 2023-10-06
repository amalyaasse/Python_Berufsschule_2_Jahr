#zweite Schulljahr
#Liste_a4
#Fußball
#Die Software enthält ein Liste mit allen Manschaftskaders
#Diese sind Spieler: Bob, Fritz, Hans, Kai, Kurt und Paul
#Sie sind genau in diese reinefolge gespeichert
#*************************************************************
#Die Software soll an einer bestimmten Stelle einen weiteren Name eintragen können
#z.B an der Stelle mit dem Index 1.
#Die Software soll folgende zwei Funktionen enthalten:
#zeige_kader() : zeigt die Namen aller Spieler im Kader in der Konsole an
#einfuegen_spieler() : fügt einen neuen Spieler an einer vom Anwender einzugebenden Stelle in die Liste ein
#Von den eingebauten Listmethoden in Python darf nur append() verwendet werden


name = ["Bob","Fritz","Hans","Kai","Kurt","Paul"]

def zeige_kader():
    print("---Kader---")
    print(name)

def ein_spieler():
    print("neue Spieler: ")
    new_name=input()
    print("index: ")
    index = int(input())
    name.insert(index,new_name) #mit insert() Funktion ist alles leichter
                                #aber in diese Aufgabe ist es verboten zu benutzen, mann darf nur append() benutzen
                                #am besten gucken die Lösung von leztes Jahr, das war besser
    
ein_spieler()
zeige_kader()

    
    


