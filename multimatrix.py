import numpy as np

def matrixMul(A, B):
    res = [[0] * len(B[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                res[i][j]  = A[i][k] * B[k][j]
    return res

def matrixMul2(A, B):
    return [[sum(a * b for a, b in zip(a, b)) for b in zip(*B)] for a in A]
a= np.zeros(shape=(100,100))
b= np.zeros(shape=(100,100))
for i in range (100):
    for j in range (100):
        a[i,j] = 12.2* (i+1) - 3.8* (j+1)
        b[i,j] = 65.1+ 3.3* (i+1) - 20.2 * (j+1)

print(a)
print('---------')
print(b)

#a = [[1,2], [3,4], [5,6], [7,8]]
#b = [[1,2,3,4], [5,6,7,8]]
#print (matrixMul(a,b))
#print (matrixMul(b,a))
#print ("-"*90)
#print (matrixMul2(a,b))
print (matrixMul2(b,a))
#print ("-"*90)

#print(map(list,dot(a,b)))
#print(map(list,dot(b,a)))

