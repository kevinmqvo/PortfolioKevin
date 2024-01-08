s=0
def f(s):
    for i in range(1,10000):
        s=s+(1/(i*i))
        print("étape",i,":",s)
    return s
print(f(s))
        
