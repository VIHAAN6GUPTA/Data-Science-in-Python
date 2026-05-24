# Importing pandas
import pandas as pd

# ------------------------------
# Version Check
# ------------------------------
print("Pandas version:", pd.__version__)  # Helpful for compatibility checking

# ------------------------------
# 1. Creating a Series from a List
# ------------------------------
a = pd.Series([2, 3, 4, 5], index=['a', 'b', 'c', 'd'])  # Custom index

# Display values of the Series
print("\nSeries a values:", a.values)          # Only values (as NumPy array)
print("Type of a.values:", type(a.values))     # <class 'numpy.ndarray'>
print("Type of a:", type(a))                   # <class 'pandas.core.series.Series'>
print("Index of a:", a.index)                  # Index object

# Slice using labels (inclusive)
print("\nSlicing Series a from 'a' to 'c':\n", a['a':'c'])

# ------------------------------
# 2. Creating a Series from Dictionary
# ------------------------------
grads_dict = {'a': 4, 'b': 5, 'c': 6}
grads = pd.Series(grads_dict)
print("\nSeries created from dictionary:\n", grads)

# ------------------------------
# 3. Creating a DataFrame from Dictionary
# ------------------------------
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Delhi', 'Mumbai', 'Bangalore']
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# ------------------------------
# 4. Exploring the DataFrame
# ------------------------------
print("\nShape of DataFrame:", df.shape)     # (rows, columns)
print("Data types:\n", df.dtypes)
df.info()  # Full summary of DataFrame

# ------------------------------
# 5. Selecting Data
# ------------------------------
print("\nSingle column - Name:\n", df['Name'])      # Accessing a column
print("Row 0 using loc:\n", df.loc[0])              # Accessing row by label
print("Row 1 using iloc:\n", df.iloc[1])            # Accessing row by index

# ------------------------------
# 6. Filtering Data
# ------------------------------
# Get rows where Age is greater than 28
filtered = df[df['Age'] > 28]
print("\nFiltered DataFrame (Age > 28):\n", filtered)

# ------------------------------
# 7. Adding Columns
# ------------------------------
# Add new column 'IsSenior' where Age > 30
df['IsSenior'] = df['Age'] > 30
print("\nDataFrame with 'IsSenior':\n", df)

# ------------------------------
# 8. Sorting
# ------------------------------
# Sort rows by Age descending
sorted_df = df.sort_values(by='Age', ascending=False)
print("\nSorted by Age descending:\n", sorted_df)

# ------------------------------
# 9. Grouping
# ------------------------------
# Group by City and calculate mean Age
grouped = df.groupby('City')['Age'].mean()
print("\nMean Age by City:\n", grouped)

# ------------------------------
# 10. File I/O with CSV
# ------------------------------
# Save DataFrame to CSV
df.to_csv('example.csv', index=False)

# Read it back
df_loaded = pd.read_csv('example.csv')
print("\nLoaded DataFrame from CSV:\n", df_loaded)

# ------------------------------
# 11. Handling Missing Data
# ------------------------------
# Creating a DataFrame with NaN values
nan_data = {
    'A': [1, 2, None],
    'B': [None, 5, 6]
}
df_nan = pd.DataFrame(nan_data)
print("\nDataFrame with NaN values:\n", df_nan)

# Fill missing values with 0
print("\nFilled NaN with 0:\n", df_nan.fillna(0))

# Drop rows with any NaNs
print("Dropped rows with NaNs:\n", df_nan.dropna())
