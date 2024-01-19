def twoSum(nums: list[int], target: int) -> list[int]: 
    
    hashMap = {}

    for index, currentNumber in enumerate(nums):
        difference = target - currentNumber
        if difference in hashMap:
            return index, hashMap[difference]
        else:
            hashMap[currentNumber] = index

# Time complexity: worst case is O(n) because we have to iterate through the entire list
# Space: O(n) because we created a hash map to store key/value pairs
        
print(twoSum([2,7,11,15], 9))

