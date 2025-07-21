# Search in a 2D matrix where each row and column is sorted
# 🔸 Real-world use: image matrix, confusion matrix, token embedding

def search_matrix(matrix, target):
    if not matrix:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    row = 0
    col = cols - 1  # Start from top-right corner

    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif target < matrix[row][col]:
            col -= 1  # Move left
        else:
            row += 1  # Move down

    return False

matrix = [
    [1, 4, 7],
    [10, 11, 16],
    [20, 23, 30]
]

print("Found 11?", search_matrix(matrix, 11))
print("Found 5?", search_matrix(matrix, 5))