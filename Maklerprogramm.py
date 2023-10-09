#Eingabe: Grundstückslänge un -Breite, Quadratmetrpreis, Maklerprovision in %, aktueller umsatzsteuer in %
#Ausgabe: Grundstückpreis und Maklerprovision

lange =float(input("Grundstücklänge: "))
b =float(input("Grundstückbreite: "))
p =float(input("Quadratmetrpreis: "))
m = float(input("Maklerprovision in Prozent: "))
u = float(input("Umsatzsteuer in Prozent: "))


# Grundstückpreis mit Umsatzsteuer
g = lange*b*p + (lange*b*p)*u/100

#Maklerprovision

makler = g*m/100


print("-----------------Berechnungen------------------------------")
print("Grundstückpreis: ", g)
print("Maklerprovision: ", g*m/100)