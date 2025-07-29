import numpy as np
# 1d array
numbers = np.array([34, 33, 29, 28, 27])
print(numbers)

# Array containing different heights in centimeters
heights = np.array([185, 170, 192, 178, 175])

# Array containing different weights in kilograms
weights = np.array([75, 68, 82, 70, 77])
print(heights)
print(weights)

# 2d array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

# 2D array where rows represent different people and columns represent different measurements (height, weight)
measurements = np.array(
    [[185, 75], [170, 68], [192, 82], [178, 70], [175, 77]])
print(measurements)

# 3d arrays
# A 3D array, also known as a tensor, is a collection of 2D arrays arranged in layers.
# To create a 3D array, you can pass a list of lists of lists to the np.array() function:

tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(tensor)


# let's create zeros with special arrays:
zeros = np.zeros((2, 2))
print("You Succesfully created zeros:\n", zeros)

ones = np.ones((3, 3))
print("Here are the ones you requested: \n", ones)

only_seven = np.full((3, 3), 7)
print("You will find 9 sevens : \n", only_seven)
