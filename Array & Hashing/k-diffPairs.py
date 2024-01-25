def findPairs(nums: list[int], k: int) -> int:
    hashMap = {}
    count = 0
    for num in nums:
        hashMap[num] = 1 + hashMap.get(num, 0)

    if k == 0:
        for value in hashMap.values():
            if value > 1:
                count += 1
    else:
        for key, value in hashMap.items():
            if key - k in hashMap:
                count += 1
    
    return count


