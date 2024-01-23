def generateMatrix(n: int) -> list[list[int]]:
    output = [[0] * n for _ in range(n)]

    rows = len(output)
    cols = len(output[0])

    direction = 1
    count = 1
    i = 0
    j = -1

    while rows > 0 and cols > 0:
        for _ in range(cols):
            j += direction 
            output[i][j] = count
            count += 1
        
        rows -= 1

        for _ in range(rows):
            i += direction
            output[i][j] = count
            count += 1
        
        cols -= 1

        direction *= -1 
    
    return output 
