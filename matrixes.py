import numpy as np

# 1 dimension
a = np.array([1, 2, 3])
print(a.size, a.shape)

# 2D - 2x3
b = np.array([[1, 2, 3], [2, 4, 6]])
print(b.size, b.shape)

print(np.zeros((2, 3), dtype=complex))

print(np.eye(3, dtype=np.int64))

