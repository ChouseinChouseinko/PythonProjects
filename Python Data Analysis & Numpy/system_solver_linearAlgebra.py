import numpy as np
# 2x + 3y =39
# 5x -y =-1

a = np.array([[2, 3], [5, -1]])  # this are the A
b = np.array([39, -1])

# now we need to solve this system

solution = np.linalg.solve(a, b)
print(solution)
