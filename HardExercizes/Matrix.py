numero = int(input("Insert a number and i ll make a identity matrix with the row of the number inserted"))
identity = lambda n : [1 if x == y else 0 for x in range(n) for y in range(n)]
print(identity(numero))
matrixMaker = lambda matrix,n,m: [[matrix[j + i * m] for j in range(0, m)] for i in range(0, n)]
print(matrixMaker(identity(numero), numero, numero))

A = [[1,2,3], [4,5,6]]
print(A)
print("Trasposta di A")
TA = matrixMaker([A[x][y] for x in range(len(A)) for y in range(len(A[0]))], len(A[0]), len(A))
print(TA)

elem=lambda A,B,i,j: sum([A[i][k]*B[k][j] for k in range(len(A[0]))])
multiply=lambda A, B: matrixMaker(
[elem(A,B,i,j) for i in range(len(A)) for j in range(len(B[0]))], len(A), len(B[0]))