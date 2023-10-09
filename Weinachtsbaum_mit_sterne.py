#Mithilfe von zwei Schleifen n zeilen mit je m Sterne angeben
n = int(input("Der Zahl der Sterne angeben: "))
m = int(input("Der Zeile angeben: "))

"""for i in range (n):
    for j in range (m):
        print("*",end=" ")
    print("77")
   """

for i in range(1,n):
   for j in range(1,m):
       print("*"*i)
          