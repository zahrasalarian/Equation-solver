import numpy as np
import sys, math

# Number of equations
print("Please enter Number of equations")
num_of_rows = int(input())

# making Coefficients matrix
print("Please enter coefficients matrix line by line")
matrix = []
for _ in range(num_of_rows):
    row = list(map(int,input().split()))
    matrix.append(row)
print("Please enter constant matrix in one line")
B = list(map(int,input().split()))

# making augmented matrix
for a,b in zip(matrix,B):
    a.append(b)
A = np.array(matrix, dtype=np.float64)
print("Augmented Matrix")
print(A)

# making echelon form
pivot_positions = []
for i in range(A.shape[0] ):
    key = i
    mark = 0
    while(key < A.shape[1] and mark != 1):
        for n in A[i:,key]:
            if n != 0:
                mark = 1
                break
        if mark != 1:
            key += 1
    if key== A.shape[1] and i == A.shape[0] - 1:
        pass
    else:
        temp = [i, key]
        pivot_positions.append(temp)
    for j in range(i+1,A.shape[0]):
        if A[i ,key ] == 0:
            temp = np.array(A[A.shape[0] - 1], dtype=np.float64)
            A[A.shape[0] - 1] = A[i]
            A[i] = temp
        if A[j, key] == 0:
            continue
        coefficient = -(A[j, key]/A[i, key])
        A[j] = A[i]*coefficient + A[j]
        print("**********************")
        print(A)

# final row echelon form
print("final echelon form")
A = A.astype(np.int64)
print(A)

# making reduced echelon form
A = A.astype(np.float64)
for p in reversed(pivot_positions):
    A[p[0]] = A[p[0]] / A[p[0], p[1]]
    for i in range(p[0] - 1,-1,-1):
        coefficient = -(A[i, p[1]] / A[p[0], p[1]])
        A[i] = A[p[0]]*coefficient + A[i]

for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        if abs(A[i,j] - int(A[i,j])) > 0.5 and A[i,j]<0:
            A[i,j] = math.floor(A[i,j])
        elif abs(A[i,j] - int(A[i,j])) <= 0.5 and A[i,j]<0:
            A[i,j] = math.ceil(A[i,j])
        elif abs(A[i,j] - int(A[i,j])) > 0.5 and A[i,j]>0:
            A[i,j] = math.ceil(A[i,j])
        elif abs(A[i,j] - int(A[i,j])) <= 0.5 and A[i,j]>0:
            A[i,j] = math.floor(A[i,j])
print("reduced echelon form")
A = A.astype(np.int64)
print(A)

# check if matrix has no solution
if A[A.shape[0] - 1 ,A.shape[1] - 1] !=0 and A[A.shape[0] - 1 ,A.shape[1] - 2] == 0:
    print("inconsistent")
    sys.exit()

# finding answers
ans_list = []
col_vector_ans = []
for p in pivot_positions:
    ans_str = "X{} =".format(p[1] + 1)
    col_vector_ans_str = ""
    count = p[1]
    for a in A[p[0] , p[1] + 1:A.shape[1] - 1]:
        if a == 0:
            count += 1
        else:
           ans_str += " + ({}X{})".format(-a,count + 2)
           col_vector_ans_str += "+ ({}X{})".format(-a,count + 2)
           count += 1
    ans_str += " + ({})".format(A[p[0] , A.shape[1] - 1])
    col_vector_ans_str += " + ({})".format(A[p[0] , A.shape[1] - 1])
    ans_list.append(ans_str)
    col_vector_ans.append(col_vector_ans_str)
# printing answers
print("answers")
for ans in ans_list:
    print(ans)

# showing answers in Column vector form
print("answers in Column vector form")
answers = np.array(col_vector_ans)
print(np.reshape(answers,(-1,1)))