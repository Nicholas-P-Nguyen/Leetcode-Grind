def rotate(matrix: list[list[int]]) -> None:
    left = 0
    right = len(matrix) - 1

    while left < right:
        # Only rotating n-1 times
        for i in range(right - left):
            top = left
            bottom = right

            # Save the value of top left
            topLeft = matrix[top][left + i]
            
            # top left is assigned to bottom right 
            matrix[top][left + i] = matrix[bottom - i][left] 

            # bottom left is assigned to bottom right
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # bottom right is assigned to top right
            matrix[bottom][right - i] = matrix[top + i][right]

            # top right is assigned to the saved value 
            matrix[top + i][right] = topLeft

        left += 1
        right -= 1
