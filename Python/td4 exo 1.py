mat=[[12,1,0],[1,4,1],[12,1,0],[1,4,1],[1,0,0],[1,4,1],[1,0,0],[1,4,1],[1,0,0]]
n=len(mat)
m=len(mat[0])
for i in range (0,n):
    for y in range (0,m):
        print("mat[",i,",",y,"]:",mat[i][y])
