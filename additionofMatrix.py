A = [[1,2,3],[1,2,3],[1,2,3]]
B = [[1,1,1],[2,2,2],[3,3,3]]
C = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A)) : 
    for j in range(len(A[i])): 
        C[i][j] = A[i][j] + B[i][j] 
# print(C)
for r in C: print(r)

