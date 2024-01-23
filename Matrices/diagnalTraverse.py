def findDiagnalOrder(matrix: list[list[int]]) -> list[int]:
    # Pointers and how we index into matrix. 
    # i is the row index, j is the column index.
    i = 0
    j = 0

    rows = len(matrix)
    cols = len(matrix[0])
    output = []

    goingUp = True

    while len(output) != (rows * cols):
        if goingUp:
            while i >= 0 and j < cols:
                output.append(matrix[i][j])
                i -= 1
                j += 1

            if j == cols:
                j -= 1
                i += 2
            else:
                i += 1
            
            goingUp = False
        
        else:
            while i < rows and j >= 0:
                output.append(matrix[i][j])
                j -= 1
                i += 1
                
            
            if i == rows:
                j += 2
                i -= 1
            else:
                j += 1
        
            goingUp = True

    return output


    