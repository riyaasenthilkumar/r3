def countNumbersWith4(n) :
    result = 0 
    for x in range(1, n + 1) :
        if(has4(x) == True) :
            result = result + 1
    return result
def has4(x) :
    while (x != 0) :
        if (x%10 == 4) :
            return True
        x = x //10
     
    return False
n = 328
print ("Count of numbers from 1 to ", n,
        " that have 4 as a a digit is ", 
                    countNumbersWith4(n)) 
 
 
