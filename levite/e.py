import numpy as np  

def matrix_power(matrix, n):
    if n == 0:
        return np.eye(2)
    if n % 2 == 0:
        half = matrix_power(matrix, n // 2)
        return np.dot(half, half)
    else:
        return np.dot(matrix, matrix_power(matrix, n - 1))

fib_matrix = np.array([[1, 1], [1, 0]])
def fib(n):
    if n == 0:
        return 0
    # F_n is in the [0][0] position of fib_matrix^(n-1)
    return matrix_power(fib_matrix, n-1)[0][0] 
# Example: fib(10) = 55