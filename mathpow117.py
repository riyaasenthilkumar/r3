import  math
n=int(input("enter num"))
b=1
while(n!=0):
a=n%10
b=b+mathpow(b,a)
print(b)
n=n//10
print(b)
