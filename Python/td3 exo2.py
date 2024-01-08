t=[6,12,9,1,50,10,8,3,4,13]
n=len(t)
print(n)
m=t[0]
for i in range(1,n):
    if t[i]>m: 
        m=t[i]

print("le maximum est",m)
    

