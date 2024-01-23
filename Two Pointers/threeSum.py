def threeSum(nums: list[int]) -> list[list[int]]:
    output = []
    nums.sort()

    for currentIndex, currentNumber in enumerate(nums):
        # Checking for duplicates. If the previous number is the same as current number go to the next iteration
        if currentIndex > 0 and nums[currentIndex - 1] == currentNumber:
            continue

        left = currentIndex  + 1
        right = len(nums) - 1
        while left < right:
            totalSum = currentNumber + nums[left] + nums[right]
            if totalSum > 0: 
                right -= 1
            elif totalSum < 0:
                left += 1
            else:
                output.append([currentNumber, nums[left], nums[right]])
                # Incrementing left pointer after we found the total sum that equals 0
                left += 1
                # Checking for duplicates. If after we increment left and the value is same as previous we increment left again 
                while nums[left - 1] == nums[left] and left < right:
                    left += 1
    return output

# Time complexity: O(n logn) to sort the array and O(n^2) where we iterate through the array twice. Once to find the first number and a second to find the second and third number


threeSum([-1, 0, 1, 2, -1, -4])