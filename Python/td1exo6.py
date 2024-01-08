m=float(input("saisir année"))
print ("m",m)
n= (m-1900)
print(n)
a=(n%19)
print("a",a)
b=(a*7+1)//19
print("b",b)
c=((11*a)-b+4)%29
print("c",c)
d=n//4
print(d)
e=(n-c+d+31)%7
print(e)
p=(25-c-e)
print(p)
g=31
h=0
if p>0:date=(h+p)
if p<0:date=(g+p)
else:date=31
print(date,"mars")
