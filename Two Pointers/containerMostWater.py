def containerWithMostWater(height: list[int]) -> int:
    maxArea = 0
    left = 0 
    right = len(height) - 1

    while left < right:
        y = min(height[left], height[right]) 
        x = right - left
        currentArea = x * y
        maxArea = max(maxArea, currentArea)

        # If the height are equal, check to see neighbor heights and see which one is bigger 
        if height[left] == height[right]:
            if height[left + 1] > height[right - 1]:
                left += 1
            else:
                right -= 1
        # If left height is bigger keep it in place 
        elif height[left] > height[right]:
            right -= 1
        # If right height is bigger keep it in place
        else:
            left += 1
    
    return maxArea

print(containerWithMostWater([1, 8, 6, 2, 5, 4, 8, 3, 7]))


'''
Time complexity: O(n) where n is the size of the input array. 
With the 2-pointers approach we only have to iterate through the array one time 

Space complexity: O(1) We don't use any extra data structures 
'''

def neetsolution(height: list[int]) -> int:
    maxArea = 0
    left = 0 
    right = len(height) - 1

    while left < right:
        y = min(height[left], height[right]) 
        x = right - left
        currentArea = x * y
        maxArea = max(maxArea, currentArea)

        if height[left] < height[right]:
            left += 1
        # It doesn't matter which pointer we move if the pointers are equal 
        else:
            right -= 1
    
    return maxArea