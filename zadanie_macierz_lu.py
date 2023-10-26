import numpy as np
import numpy.random as rnd

# Warunki zadania i wygenerowanie A i B
m = rnd.randint(2, 10)
n = m + rnd.randint(0, 3)
e = []
for _ in range(n):
    if rnd.uniform(-5, 5) != 0:
        e.append(rnd.uniform(low=-5, high=5))
B = np.matrix([e])

A = np.zeros((n, m))
for i in range(0, n):
    for j in range(0, m):
        if i < j:
            A[i, j] = rnd.uniform(low=-1, high=1)
        elif i == j:
            A[i, j] = rnd.uniform(low=-3, high=3)
        else:
            A[i, j] = rnd.uniform(low=0, high=1)
print("A: ")
print(A)
print("B: ")
print(B)
print("Liczba kolumn: ")
print(m)
print("Liczba wierszy: ")
print(n)

# Dekompozycja macierzy LU
# Macierz U - lower triangle
U = np.array(A, copy=True)
factors = np.zeros((n, n))

for x in range(0, len(U[0])):
    for y in range(x, len(U)):
        if x != y and U[x][x] != 0 and U[y][x] != 0:
            factor = U[y][x] / U[x][x]
            factors[y][x] = factor
            U[y] = (-factor * U[x]) + U[y]
print("Macierz U: ")
print(U)

# Macierz L - upper triangle
L = np.zeros((n, n))
for x in range(0, len(L)):
    for y in range(0, len(L)):
        if x == y:
            L[y][x] = 1
        elif x > y:
            L[y][x] = 0
        elif x < y:
            L[y][x] = factors[y][x]
print("Macierz L: ")
print(L)

# Sprawdzenie, czy L * U = A
arr_L = np.array(L, copy=True)
arr_U = np.array(U, copy=True)
print("L * U ")
print(np.dot(arr_L, arr_U))
print("A: ")
print(A)

# Wyliczanie Y - forward substitution
# L * Y = B
Y = np.zeros(n)
arr_B = np.array(B, copy=True).flatten()

for i in range(0, n, 1):
    subs = []
    subs.append(-arr_B[i])
    j = 0
    while j < i != 0:
        subs.append(L[i, j]*Y[j])
        j += 1

    res_subs = 0
    for sub in subs:
        res_subs -= sub
    Y[i] = res_subs / L[i, i]

print("Y: ")
print(Y)


# Wyliczanie X - backward substitution
# U * X = Y
X = np.zeros(n)

for i in range(m - 1, -1, -1):
    tmp = Y[i]
    for j in range(i + 1, m):
        tmp -= U[i, j] * X[j]
    X[i] = tmp / U[i, i]
X = X[X != 0]
print("X: ")
print(X)

# Wyliczenie wektora B powstałego z A i X
# A * X = B
B_res = np.dot(A, X)
print("Powstały wektor B: ")
print(B_res)

# Wektor I - odejmowanie powstałego wektora B od wektora B z zadania
I = arr_B - B_res
print("Wektor I: ")
print(I)

# Norma euklidesowa - wektor I * wektor I
res = np.dot(I,I)
print("Wynik: ")
print(res)
