import numpy as np

# Create random arrays
A_1 = np.random.randint(50, 100, 10)
A_2 = np.random.randint(50, 100, 10)

print("Array 1:", A_1)
print("Array 2:", A_2)

# 1. Sum
print("Sum:", A_1 + A_2)

# 2. Dot product
print("Dot Product:", A_1.dot(A_2))

# 3. Cross product (only first 3 elements, because cross requires 3D vectors)
print("Cross Product (first 3 elements):", np.cross(A_1[:3], A_2[:3]))

# 4. Element-wise multiplication
print("Element-wise Multiplication:", A_1 * A_2)

# 5. Transpose (1D array transpose is itself)
print("Transpose of A_1:", A_1.T)

# 6. Element-wise addition
print("Element-wise Addition:", A_1 + A_2)

# 7. Element-wise subtraction
print("Element-wise Subtraction:", A_1 - A_2)

# 8. Element-wise multiplication (again)
print("Element-wise Multiplication:", A_1 * A_2)

# 9. Element-wise division
print("Element-wise Division:", A_1 / A_2)

# 10. A_1 squared
print("A_1 squared:", A_1 ** 2)

# 11. Square root of A_2
print("Square Root of A_2:", np.sqrt(A_2))

# 12. Exponential of A_1
print("Exponential of A_1:", np.exp(A_1))

# 13. Natural logarithm of A_2
print("Natural Log of A_2:", np.log(A_2))

# 14. Absolute value of A_1
print("Absolute Values of A_1:", np.abs(A_1))

# 15. Minimum value of A_2
print("Minimum of A_2:", np.min(A_2))

# 16. Most occurring value in A_1 and A_2
print("Most occurring value in A_1:", np.bincount(A_1).argmax())
print("Most occurring value in A_2:", np.bincount(A_2).argmax())
