x=int(input("entrez x"))
def f(x):
    r=x
    for i in range (0,15):
        p=r
        r=(r+(x/r))/2
        if r!=p: 
            print("étape",i,":",r)
    return r
print(f(x))
