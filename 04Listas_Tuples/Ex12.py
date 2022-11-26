#https://aprendeconalf.es/docencia/python/ejercicios/listas-tuplas/
A = [[1,2,3], [4,5,6]]
B = [[-1,0], [0,1], [1,1]]
res = [[0, 0], [0, 0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            res[i][j] += A[i][k] * B[k][j]
for i in range(len(res)):
    res[i] = tuple(res[i])
res = tuple(res)
for i in range(len(res)):
    print(res[i])