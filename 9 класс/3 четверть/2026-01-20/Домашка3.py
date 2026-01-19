m = int(input("Строк в первой матрице: "))
n = int(input("Столбцов в первой матрице : "))
p = int(input("Столбцов во второй матрице: "))

print("\nПервая матрица:")
A = []
for i in range(m):
    row = list(map(float, input(f"Строка {i+1}: ").split()))
    A.append(row)

print("\nВторая матрица:")
B = []
for i in range(n):
    row = list(map(float, input(f"Строка {i+1}: ").split()))
    B.append(row)

C = []
for i in range(m):
    row = []
    for j in range(p):
        sum = 0
        for k in range(n):
            sum += A[i][k] * B[k][j]
        row.append(sum)
    C.append(row)

print("\nРезультат:")
for row in C:
    print((f"{x}" for x in row))
