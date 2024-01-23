def matrixReshape(matrix: list[list[int]], r: int, c: int) -> list[list[int]]:
    rows = len(matrix)
    cols = len(matrix[0])

    if rows * cols != r * c:
        return matrix
    
    # [0] * c is getting the new number of columns in the row
    # Loop is getting the new number of rows 
    output = [[0] * c for _ in range (r)]
    # Flatten the 2D array into temp array
    temp = []
    # Loop through each element in matrix to flatten matrix
    for i in range(rows):
        for j in range(cols):
            temp.append(matrix[i][j])

    # Used to increment the temp array
    k = 0
    # Reshape array with this loop 
    for i in range(r):
        for j in range(c):
            output[i][j] = temp[k]
            k += 1

    return output
