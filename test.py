import numpy as np

a = np.array([10, 20, 30, 40])

print(a)
print(a * 2)
print(a + 5)
print(a.mean())
print(a.max())
print(a[a > 20])



#Add NumPy marks practice

import numpy as np

marks = np.array([85, 90, 78, 92, 88])
print("Average marks:", marks.mean())
print("min marks:", marks.min())
print("Marks>50:", marks[marks > 50])