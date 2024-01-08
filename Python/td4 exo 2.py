mat=[[12,1,0],[1,4,1],[12,1,0],[1,4,1],[1,0,0],[1,4,1],[1,0,0],[1,4,1],[1,0,0]]
n=len(mat)
m=len(mat[0])
x=0
for i in range (0,n):
    for j in range (0,m):
        x=x+mat[i][j]
        print("sqdklqs",x)
print(x)
        
