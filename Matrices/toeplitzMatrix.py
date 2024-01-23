def isToeplitzMatrix(matrix: list[list[int]]) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return False
    
    return True