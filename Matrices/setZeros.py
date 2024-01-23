def setZeros(matrix: list[list[int]]) -> None:
    rows = len(matrix)
    columns = len(matrix[0])

    frow = False
    fcol = False

    # Checking is there are any 0s in first column
    for i in range(rows):
        if matrix[i][0] == 0:
            fcol = True

    # Checking is there are any 0s in first row 
    for i in range(columns):
        if matrix[0][i] == 0:
            frow = True
    
    # Scan row-wise, skipping the first row/col, if 0 is found set the first row and col to 0
    for i in range(1, rows):
        for j in range(1, columns):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    # Checking for 0's in the rows, if there is 0 then set the whole row to 0 
    for i in range(1, rows):
        if matrix[i][0] == 0:
            for j in range(1, columns):
                matrix[i][j] = 0
    
    # Checking for 0's in the columns, if there is 0 then set the whole column to 0 
    for j in range(1, columns):
        if matrix[0][j] == 0:
            for i in range(1, rows):
                matrix[i][j] = 0

    # Check if first row boolean is true, if so set first row to 0
    if frow:
        for j in range(columns):
            matrix[0][j] = 0
    # Check if first column boolean is true, if so set first column to 0
    if fcol:
        for i in range(rows):
            matrix[i][0] = 0


