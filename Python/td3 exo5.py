t=[6,12,9,1,5,10,8,3,4,13]
n=len(t)
x=0
for i in range (0,n):
    if t[i]>10:
        x=x+1

print("le nombre d'elm >10 du tableau est",x)
