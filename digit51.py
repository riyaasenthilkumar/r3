a=input("Enter the first number:")
b=input("Enter the second number:")
c=input("Enter the third number:")
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
  for j in range(0,3):
    for k in range(0,3):
        if(i!=j&j!=k&k!=i)
        print(a[i],a[j],a[k])
