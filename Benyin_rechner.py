#Eingabe: Literpreis Benzin, verbrauchte Liter, gefahrene km
#Ausgabe: Verbrauch pro 100 km, Preis pro 100 km, Preis der Gesamtstrecke

literpreis = float(input("Literpreis Benzin: "))
verbrauchte_liter_pro_km = float(input("verbrauchte Liter pro km: "))
km = float(input("gefahrene km: "))

print("verbrauch pro 100 km: ", verbrauchte_liter_pro_km*100," Liter")
print("Preis der Gesamtstrecke: ", literpreis*verbrauchte_liter_pro_km*km, " Euro")