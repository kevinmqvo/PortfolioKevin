m1=[[1,7],[1,7],[1,7]]
m2=[[2,6],[2,6],[2,6]]
print(m1)
print(m2)
m=len(m1)
n=len(m1[0])
x=len(m2)
y=len(m2[0])
print(m)
print(n)
print(x)
print(y)
m3=[0]*m
for i in range(0,m):
    m3[i]=[0]*n
print(m3)
print()

z=0
for i in range(0,m):
    for j in range (0,n):
        m3[i][j]=m1[i][j]+m2[i][j]
print(m3)
