def isMultipleOf13(n):
    odd_count = 0
    even_count = 0
    if(n < 0): 
        n = -n
    if(n == 0):
        return 1
    if(n == 1): 
        return 0
 
    while(n):
        if(n & 1): 
            odd_count += 1
        n = n >> 1
        if(n & 1):
            even_count += 1
        n = n >> 1
 
    return isMultipleOf13(abs(odd_count - even_count))
num = 24
if (isMultipleOf13(num)): 
    print(num, 'is multiple of 13')
else:
    print(num, 'is not a multiple of 13')
 
