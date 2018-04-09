def binaryPallindrome(num):
     binary = bin(num)
     binary = binary[2:]
     return binary == binary[-1::-1]
 
