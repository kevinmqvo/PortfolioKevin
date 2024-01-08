t=[6,12,9,1,5,10,8,3,4,13]
n=len(t)
b=[0]*n
m=t[0]
for i in range (1,n):
    if t[i]>m:
        m=t[i]
        x=(i)
print(m)
print(x)
t[x]=0
print(t)
u=t
for i in range (1,n):
    if u[i]>m:
        m=u[i]
        x=i
print(m)
