def stringumkehr(string): 
    if len(string) == 0: 
        return string 
    else: 
        return stringumkehr(string[1:]) + string[0] 
  
string = "Hund"
  
print ("The original string  is : ", string) 

print ("The reversed string is : ",stringumkehr(string)) 

    