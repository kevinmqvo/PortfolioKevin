n=int(input("Saisir une valeur entière de n"))

def f(x):
    rac=0
    while (rac+1)*(rac+1)<=n:
        rac=rac+1
    return rac
        
print(f(n))
        

