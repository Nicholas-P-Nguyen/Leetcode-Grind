def containsDuplicate(nums: list[int]) -> bool:
    seen = set()
    for number in nums:
        if number in seen: 
            return True
        seen.add(number)
    return False

# Time complexity: O(n) because we have to iterate through the whole list
# Space: O(n) make space for the numbers in the set

print(containsDuplicate([1,2,3,1]))