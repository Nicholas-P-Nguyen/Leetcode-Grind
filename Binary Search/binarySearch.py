def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2

        if nums[middle] > target:
            right = middle - 1
        elif nums[middle] < target:
            left = middle + 1
        else: 
            return middle
    
    return -1

print(search([-1, 0, 3, 5, 9, 12], 9))

'''
Time complexity: O(logn) because at each iteration we cut the input array in half 
Space complexity: O(1) no data structures used, just pointers 
'''

