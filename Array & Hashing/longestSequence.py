def longestConsecutive(nums: list[int]) -> int:
    hashSet = set(nums)
    longest = 0
    for number in hashSet:
        if (number - 1) not in hashSet:
            currentLength = 1
            while (number + currentLength) in hashSet:
                currentLength += 1
            longest = max(longest, currentLength)
    return longest

print(longestConsecutive([100, 4, 200, 1, 3, 2]))