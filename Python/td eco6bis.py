année=float(input("taper une année"))
g=année%19
print(g)
c=année//100
c_4=c//4
print(c,c_4)
e=(8*c+13)//25
print(e)
h=(19*g+c-c_4-e+15)%30
print(h)
k=h//28
print(k)
p=29//(h+1)
print(p)
q=(21-g)//11
print(q)
i=((k*p*q-1)*k+h)
print(i)
b=((année//4)+année)
print(b)
j1=((b+i+2+c_4)-c)
print(j1)
j2=j1%7
print(j2)
r=(28+i-j2)
print(r)
if r>31:print((r-31),"avril")
else: print(r,"mars")

