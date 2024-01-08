m=[[4,2],[3,3],[5,1]]
print(m)
x=len(m)
y=len(m[0])
print(x)
print(y)
print()

mt=[0]*y
for i in range (0,y):
    mt[i]=[0]*x
print(mt)
print()

for k in range (0,x):
    for z in range (0,y):
        mt[z][k]=m[k][z]
print(mt)


