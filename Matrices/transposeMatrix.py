def transpose(matrix: list[list[int]]) -> list[list[int]]:
    rows = len(matrix)
    cols = len(matrix[0])

    output = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            output[j][i] = matrix[i][j]

    return output