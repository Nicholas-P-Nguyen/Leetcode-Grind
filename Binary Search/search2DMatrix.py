def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    '''
    For the rows we're getting the length of how many Arrays are being passed through.
    [[1, 2, 3, 4, 5][6, 7, 8, 9, 10]] In this example 2 arrays are being passed through, so
    there are 2 rows. To calculate the columns we index into one of the arrays and get the 
    length, so there are 5 columns. Imagine the arrays being passed through being stacked on
    top of one another. 
    '''

    rows = len(matrix) 
    columns = len(matrix[0])
    top = 0
    bottom = rows - 1

    while top <= bottom:
        currentRow = (top + bottom) // 2

        if matrix[currentRow][-1] < target:
            top = currentRow + 1
        elif matrix[currentRow][0] > target:
            bottom = currentRow - 1
        else: 
            break 

    # If top is less than or equal to bottom then enter the if statement and return false. 
    if not (top <= bottom):
        return False

    # Found the row that the target resides, now perform another binary search on that row. 
    currentRow = (top + bottom) // 2
    left = 0 
    right = columns - 1

    while left <= right:
        middle = (left + right) // 2

        if matrix[currentRow][middle] < target:
            left = middle + 1
        elif matrix[currentRow][middle] > target:
            right = middle - 1
        else:
            return True
        
    return False

    '''
    Time complexity: O(log n) + O(log m) where n is the first binary search we performed and 
    m is the second binary search we performed on the last row

    Space complexity: O(1) No extra data structure needed 
    '''
    



