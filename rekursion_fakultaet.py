def fa(zahl):
    if zahl == 1:
        return 1
    else:
        return zahl*fa(zahl-1)
    
print("fakultet",fa(6))

