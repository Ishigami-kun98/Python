rows = lambda l, n, m: [[l[j+i*m] for j in range(0, m)] for i in range(0, n)]
rowshorizontal = lambda l, n, m:[[l[j + i *m] for i in range(0, m)] for j in range(0, n)]
identity = lambda n : rows([1 if x==y else 0 for x in range(n) for y in range(n)], n, n)
print(('point 1 is to realize a matrix identity', identity(int(input('insert a number ')))))
n = int(input('questo esercizio fa la square inserisci un numero : '))
square = [x for x in range(1, (n**2)+1)]
squarerow = rows(square,n,n)
print(squarerow)
A = [[1,2], [3,4], [5,6]]
print("facciamo la trasposta di: ", A)
trasf = [A[y][x] for x in range(len(A[0])) for y in range(len(A))]
print(rows(trasf, len(A[0]), len(A)))
print('time to multiply 2 matrix: ', A, ' and ', squarerow)
rowsMultiply = lambda A,B,i,j : sum([A[i][k] * B[k][j] for k in range(len(A[0]))])
multiply2Matrix = lambda A, B: rows(
[rowsMultiply(A,B,i,j) for i in range(len(A)) for j in range(len(B[0]))], len(A), len(B[0])
)
multiply=lambda A, B: rows(
[rowsMultiply(A,B,i,j) for i in range(len(A)) for j in range(len(B[0]))], len(A), len(B[0]))
print('The result is ', multiply(squarerow, A))
print('If we put in inverse order ', squarerow, A)
print('The result is ', multiply(A,squarerow))
