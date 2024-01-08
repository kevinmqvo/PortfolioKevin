x=int(input("entrez x"))
def f(x):
    r=x
    for i in range (0,15):           
        r=(r+(x/r))/2
        print("étape",i,":",r)
    return r
print(f(x))
