# Define a 2D list (array)
array = [[1, 2, 3], 
         [4, 5, 6], 
         [7, 8, 9]]

# Use zip(*) to transpose the array
transpose = list(map(list, zip(*array)))

# Print the transposed array
print("Transposed array using zip():")
for row in transpose:
    print(row)
