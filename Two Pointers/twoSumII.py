def twoSum(numbers: list[int], target: int) -> list[int]:
    left = 0 
    right = len(numbers) - 1

    while left < right: 
        if numbers[left] + numbers[right] > target: 
            right -= 1
        elif numbers[left] + numbers[right] < target:
            left += 1
        else: 
            return [left + 1, right + 1]

twoSum([5, 25, 75], 100)

# Time complexity: O(n) where n is the size of the input array 
# Space complexity: O(1) no DS needed just pointers 