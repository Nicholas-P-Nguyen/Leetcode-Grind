import math

def minEatingSpeed(piles: list[int], h: int) -> int:
    left = 1
    right = max(piles)
    output = 0

    while left <= right:
        bph = (left + right) // 2

        totalTime = 0
        for stack in piles:
            # math.ceil rounds up to the nearest int. 
            totalTime += math.ceil(stack / bph)
        
        if totalTime <= h:
            output = bph
            right = bph - 1
        else:
            left = bph + 1
        
    return output
         
'''
Time complexity: O(log n) where n is the size of k
Space complexity: O(1) No data structures 
'''