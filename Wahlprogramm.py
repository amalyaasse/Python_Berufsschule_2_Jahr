#Mann muss für drei Kanditaten Namen und die Anzahl der erhaltenen Stimmen angeben
#Das Programm gibt die Prozentualen Anteil der Stimmen aus

ersteName = input("erste Kandidat: ")
zweiteName = input("zweite Kanditat: ")
driteName = input("drite Kandidat: ")
stimme_eins = int(input("erhaltene Stimme für erste Kandidat: "))
stimme_zwei = int(input("erhaltener Stimme für zweite Kandidat: "))
stimme_drei = int(input("erhaltener Stimme für dritte Kandidat: "))

print ("-----------------Wahlergebnisse----------------------------")
teilnehmerzahl = stimme_eins+stimme_zwei+stimme_drei
print("insgesamt teilgennomen",teilnehmerzahl)
x = (stimme_eins/teilnehmerzahl*100)
y = (stimme_zwei/teilnehmerzahl*100)
z = (stimme_drei/teilnehmerzahl*100)
print("erste Kandidat: ",x," %")
print("zweite Kandidat: ",y," %")
print("dritte Kandidat: ",z, " %")
