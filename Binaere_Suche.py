#Bineare Suche
#In einem sortierten Feld soll ein Suchwert gefunden werden.
def binaereSuche(x, nums):
    low = 0 #untere Grenze festlegen
    high = len(nums)-1 #obere Grenze
    
    #solange es einen Suchbereich gibt
    #die Mitte des Suchbereichs bestimmen
    while low <= high:
        mid = (low + hight) // 2
        #bei Übereinstimmung Position zurückgeben
        if x== nums[mid]:
            return mid
        #x in unteren Suchbereich: obere Grenze verschieben
        elif x< mus[mid]:
            high = mid - 1
        #x in oberen Suchbereich: untere Grenze verschieben
        else:
            low = mid + 1
#x nicht in Liste gefunden
    return -1


            
        
        
        
        
        
    
    