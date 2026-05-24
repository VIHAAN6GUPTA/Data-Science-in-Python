import numpy as np  # NumPy is Python's library for numerical computing

# 🔸 1. Creating Arrays
arr1 = np.array([1, 2, 3])                # 1D array
arr2 = np.array([[1, 2], [3, 4]])         # 2D array (matrix)
print("1D Array:", arr1)                  # ➜ [1 2 3]
print("2D Array:\n", arr2)                # ➜ [[1 2] [3 4]]

# 🔸 2. Checking Array Info
print("Shape:", arr2.shape)               # ➜ (2, 2)
print("Size:", arr2.size)                 # ➜ 4
print("Data Type:", arr2.dtype)           # ➜ int64 (or system default)

# 🔸 3. Data Type Examples
arr_float = np.array([1.2, 3.4])
arr_complex = np.array([1, 2], dtype='complex')
print("Float array:", arr_float)          # ➜ [1.2 3.4]
print("Complex array:", arr_complex)      # ➜ [1.+0.j 2.+0.j]

# 🔸 4. Special Array Creators
print("Zeros:\n", np.zeros((2, 2)))       # ➜ Matrix of 0s
print("Ones:\n", np.ones((2, 2)))         # ➜ Matrix of 1s
print("Full (5s):\n", np.full((2, 2), 5)) # ➜ Matrix filled with 5
print("Identity:\n", np.eye(3))           # ➜ 3x3 Identity matrix
print("Diagonal:\n", np.diag([1, 2, 3]))  # ➜ Diagonal matrix
print("Lower Triangle:\n", np.tri(3))     # ➜ Lower triangle matrix

# 🔸 5. Array from Range
print("arange:", np.arange(0, 10, 2))     # ➜ [0 2 4 6 8]
print("linspace:", np.linspace(0, 1, 5))  # ➜ [0.  0.25 0.5 0.75 1.]

# 🔸 6. Reshape, Transpose, Flatten
a = np.arange(12).reshape(3, 4)
print("Original 3x4:\n", a)
print("Transposed:\n", a.T)               # ➜ Flips rows/cols
print("Flattened:", a.ravel())            # ➜ 1D view
print("Reshaped (2x6):\n", a.reshape(2, 6))

# 🔸 7. Arithmetic on Arrays
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print("Add:", np.add(x, y))               # ➜ [5 7 9]
print("Subtract:", np.subtract(y, x))     # ➜ [3 3 3]
print("Multiply:", np.multiply(x, y))     # ➜ [4 10 18]
print("Divide:", np.divide(y, x))         # ➜ [4. 2.5 2.]
print("Power:", np.power(x, 2))           # ➜ [1 4 9]
print("Mod:", np.mod(y, x))               # ➜ [0 1 0]

# 🔸 8. Trigonometry
angles = np.array([0, np.pi/2, np.pi])
print("Sine:", np.sin(angles))            # ➜ [0. 1. 0.]
print("Cosine:", np.cos(angles))          # ➜ [1. 0. -1.]

# 🔸 9. Aggregation Functions
data = np.array([[1, 2], [3, 4]])
print("Mean:", np.mean(data))             # ➜ 2.5
print("Median:", np.median(data))         # ➜ 2.5
print("Std Dev:", np.std(data))           # ➜ ~1.118
print("Variance:", np.var(data))          # ➜ 1.25
print("Min:", np.min(data))               # ➜ 1
print("Max:", np.max(data))               # ➜ 4
print("Argmin:", np.argmin(data))         # ➜ 0 (index of 1)
print("Argmax:", np.argmax(data))         # ➜ 3 (index of 4)

# 🔸 10. Axis-Based Operations
print("Row Sums:", data.sum(axis=1))      # ➜ [3 7]
print("Column Sums:", data.sum(axis=0))   # ➜ [4 6]

# 🔸 11. Boolean Indexing
arr = np.array([10, 15, 20, 25])
print("Greater than 18:", arr[arr > 18])  # ➜ [20 25]

# 🔸 12. Fancy Indexing
idxs = [0, 2]
print("Selected Elements:", arr[idxs])    # ➜ [10 20]

# 🔸 13. Sorting and Searching
unsorted = np.array([30, 10, 20])
print("Sorted:", np.sort(unsorted))       # ➜ [10 20 30]
print("Argsort (indices):", np.argsort(unsorted))  # ➜ [1 2 0]
print("Where >15:", np.where(arr > 15))   # ➜ (array([2, 3]),)

# 🔸 14. Set Operations
a = np.array([1, 2, 3, 4])
b = np.array([3, 4, 5, 6])
print("Union:", np.union1d(a, b))         # ➜ [1 2 3 4 5 6]
print("Intersection:", np.intersect1d(a, b))  # ➜ [3 4]
print("Difference (A-B):", np.setdiff1d(a, b))  # ➜ [1 2]

# 🔸 15. Random Module
np.random.seed(0)  # Same random every time
print("Random Ints:", np.random.randint(1, 10, (2, 3)))
print("Random Floats:", np.random.random((2, 2)))
print("Random Normal:", np.random.randn(2))  # Standard normal

# 🔸 16. Broadcasting
a = np.array([[1], [2], [3]])
b = np.array([10, 20, 30])
print("Broadcasted Add:\n", a + b)
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]

# 🔸 17. Linear Algebra (Matrix Math)
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[2, 0], [1, 2]])
print("Dot Product:\n", np.dot(mat1, mat2))    # ➜ [[4 4] [10 8]]
print("Matrix Multiply:\n", mat1 @ mat2)       # Same
print("Transpose:\n", mat1.T)
print("Inverse:\n", np.linalg.inv(mat1))       # ➜ [[-2. 1.][1.5 -0.5]]
print("Determinant:", np.linalg.det(mat1))     # ➜ -2.0
print("Eigenvalues:", np.linalg.eigvals(mat1)) # ➜ [5.37, -0.37]
print("Rank:", np.linalg.matrix_rank(mat1))    # ➜ 2

# 🔸 18. Save & Load Arrays
np.save("my_array.npy", arr1)
loaded = np.load("my_array.npy")
print("Loaded from File:", loaded)             # ➜ [1 2 3]

# Load data from a text file named 'data.txt', using comma as delimiter
filedata = np.genfromtxt('data.txt', delimiter=',')

# Convert the loaded data to integer type (32-bit)
filedata = filedata.astype('int32')

# Print the resulting NumPy array
print(filedata)

# 🔸 19. Copy vs View
a = np.array([1, 2, 3])
view = a.view()
copy = a.copy()
a[0] = 100
print("Original:", a)                          # [100 2 3]
print("View (shares data):", view)             # [100 2 3]
print("Copy (independent):", copy)             # [1 2 3]

# Create a 1D NumPy array with elements [1, 2, 3, 4]
v1 = np.array([1, 2, 3, 4])

# Create another 1D NumPy array with elements [5, 6, 7, 8]
v2 = np.array([5, 6, 7, 8])

# Stack the arrays vertically (row-wise) using vstack
# This creates a 2D array with each array as a new row
print(np.vstack([v1, v2, v1, v2]))


# Problem 1
# Create a 5x5 array filled with ones
output = np.ones((5, 5))
print(output)  # Print the 5x5 array of ones

# Create a 3x3 array filled with zeros
z = np.zeros((3, 3))
# Set the center element of the 3x3 array to 9
z[1, 1] = 9
print(z)  # Print the 3x3 array with 9 in the center

# Replace the center 3x3 portion of the 5x5 array with the 3x3 array `z`
output[1:-1, 1:-1] = z
print(output)  # Print the modified 5x5 array
