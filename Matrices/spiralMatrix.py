def spiralOrder(matrix: list[list[int]]) -> list[int]:
    # If direction = 1, we go left to right or top to bottom
    # If direction = -1, we go right to left or bottom to top
    direction = 1
    # Total number of rows and cols 
    rows = len(matrix)
    cols = len(matrix[0])
    # Pointers to help us traverse matrix & index into array
    # i allows us to traverse along the rows (top to bottom & bottom to top)
    i = 0
    # j allows us to traverse along the columns (left to right & right to left)
    j = -1

    output = []

    while rows > 0 and cols > 0:
        # Traversing along the rows
        for _ in range(cols):
            j += direction
            output.append(matrix[i][j])
            # |1|2|3| i is currently 0, and j will increment by 1. By the end of this loop it j will be 2.
        # Decrement rows by 1 since one less cell in the column needs to be visited
        rows -= 1

        # Traversing along the columns 
        for _ in range(rows):
            i += direction              # |1|2|3| j is still 2, but i is getting incremented,
            output.append(matrix[i][j]) # |4|5|6| allowing us to append 6 and 9.
                                        # |7|8|9|  
        # Decrement cols by 1 since one less cell in the row needs to be visited 
        cols -= 1

        # Change direction now. 
        direction *= -1
    
    return output



