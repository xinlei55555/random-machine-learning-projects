import numpy as np

#matrix multiplication
A = np.array([[1, -1, 0], [2, -2, 0]])
print(A)

#transposing the previous array
AT = A.T
print(AT)

#weights
W=np.array([[3,5,7,9],[2,4,6,8]])

#matrix multiplication
Z=np.matmul(AT, W)
print(Z)

#I can even add bias
B=np.array([[165, 123, 125, 125], [165, 123, 125, 125], [165, 123, 125, 125]])
Z=Z+B
print(Z)