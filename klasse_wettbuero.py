class Wettschein:
    def __init__(self,namePerson,nameRennPferd,wetteinsatz,gewinnfaktor):
        self.namePerson = namePerson
        self.nameRennPferd = nameRennPferd
        self.wetteinsatz = wetteinsatz
        self.gewinnfaktor = gewinnfaktor
    def getNamePerson(self):
        return self.namePerson
    def getNameRennPferd(self):
        return self.nameRennPferd
    def getWetteinsatz(self):
        return self.wetteinsatz
    def getGewinnfaktor(self):
        return self.gewinnfaktor

wettschein1 =Wettschein("Ron","Klopf",100,12)
print(wettschein1.getNamePerson(),wettschein1.getNameRennPferd(), wettschein1.getWetteinsatz(),wettschein1.getGewinnfaktor())
        