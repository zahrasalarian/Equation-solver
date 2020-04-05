import numpy as np
import sys

# Number of equations
num_of_rows = int(input("Please enter Number of equations"))

# making Coefficients matrix
print("Please enter coefficients matrix line by line")
matrix = []
for _ in range(num_of_rows):
    row = list(map(int, input().split()))
    matrix.append(row)

A = np.array(matrix, dtype=np.float64)
print("Matrix")
print(A)

# making echelon form
pivot_positions = []
for i in range(A.shape[0]):
    key = i
    mark = 0
    while (key < A.shape[1] and mark != 1):
        for n in A[i:, key]:
            if n != 0:
                mark = 1
                break
        if mark != 1:
            key += 1
    if key == A.shape[1] and i == A.shape[0] - 1:
        pass
    else:
        temp = [i, key]
        pivot_positions.append(temp)
    for j in range(i + 1, A.shape[0]):
        if A[i, key] == 0:
            temp = np.array(A[A.shape[0] - 1], dtype=np.float64)
            A[A.shape[0] - 1] = A[i]
            A[i] = temp
        if A[j, key] == 0:
            continue
        coefficient = -(A[j, key] / A[i, key])
        A[j] = A[i] * coefficient + A[j]
        print("**********************")
        print(A)

# final row echelon form
print("final echelon form")
A = A.astype(np.int32)
print(A)

# calculating the rank of the matrix
print("Rank of the matrix = {}".format(len(pivot_positions)))

# calculating dimNullA using the Rank theorem
print("Dim(NullA) = {}".format(A.shape[1] - len(pivot_positions)))
