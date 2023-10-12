#Funktion bineare Suche
#Funktion mein
    #def mein()
    #Inhalt des Worterbuchs in Liste eintragen
    #neue Meldungen in Liste unbekant eintragen
    #liste in Datei unbekant schreiben
    #Text in Wortliste
    #Funktiion bineareSuche
    #Funktion mein

def mein():
    worterbuch = []
    infile = open("worterbuch","r")
    for line in infile:
        worterbuch.append(line[:-1])# -1 ist in bineare suche ist die lezte suche
    infile.close()
    
#Text in Worteliste überführen
worterliste = []
infile = open("text","r")
inText = infile.read()
infile.close()
wortliste = inText.split()

#
unbekant = []
for wort in wortliste:
    suchergebniss = bineareSuche(wort,woerterbuch)
    if suchergebniss == -1:
        unbekannt.append(wort)

#Liste in Datei 

    
    