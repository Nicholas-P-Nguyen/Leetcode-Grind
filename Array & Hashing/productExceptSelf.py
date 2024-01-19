def productExceptSelf(nums: list[int]) -> list[int]:
    # Space complexity: O(n) where n is the number of elements in the answer array 
    answer = [0] * len(nums)

    prefix = 1
    # Time complexity: O(n) where n is length of nums array 
    for i in range(len(nums)):
        answer[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    # Time complexity: O(n) where n is length of nums array 
    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= postfix
        postfix *= nums[i]
    
    return answer

print(productExceptSelf([5,2,4,5]))