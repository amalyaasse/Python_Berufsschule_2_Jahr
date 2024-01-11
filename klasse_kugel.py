import math

class Kugel:
    def __init__(self,radius):
        self.radius = radius
    def getRadius(self):
        return self.radius
    def oberflaeche(self):
        return 4*math.pi*self.radius**2
    def volumen(self):
        return (4/3)*math.pi*self.radius**3

Kugel1 = Kugel(5)
print("Radius:",Kugel1.getRadius())
print("oberflaeche:",Kugel1.oberflaeche())
print("volumen:",Kugel1.volumen())