def findMin(nums: list[int]) -> int:
    left = 0 
    right = len(nums) - 1
    output = nums[0]
    while left <= right: 
        if nums[left] < nums[right]:
            output = min(nums[left], output)
            break

        middle = (left + right) // 2
        output = min(output, nums[middle])
        if nums[middle] >= nums[left]: 
            left = middle + 1
        elif nums[middle] <= nums[right]:
            right = middle - 1

    return output


findMin([3,1,2])

    

