import numpy as np

m = np.array([[1, 2, 3],
              [4, 5, 6]])

print(m)
print(m.shape)
print(m[0, 1])
print(m[:, 2])
print(m.sum(axis=0))
print(m.sum(axis=1))