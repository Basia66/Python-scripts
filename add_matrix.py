M = [[1, 3, 2], [-1, 2, 6]]
N = [[3, 9, 8], [1, 0, -1]]
result = [[0, 0, 0], [0, 0, 0]]


def add_matrix(A, B):
    if len(A) != len(B):
        return "Nie da się dodać tych dwóch macierzy"
    else:
        for m in range(len(M)):
            for n in range(len(N)):
                result[m][n] = M[m][n] + N[m][n]
    return result


print(add_matrix(M, N))
