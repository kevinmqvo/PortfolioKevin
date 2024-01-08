s=0
temp=s
n=1
print(s)
while (s-temp)>0.00001:
    n=n+1
    temp=s
    s=s+(1/(n*n))
    print("étape",n,":",s)
        
