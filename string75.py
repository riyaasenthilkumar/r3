s = "this is a string"

l = list(s)  

l[1] = ""    
l[1:2] = []  
del(l[1])    

p = l.index("a")  
del(l[p])        

s = "".join(l) 
