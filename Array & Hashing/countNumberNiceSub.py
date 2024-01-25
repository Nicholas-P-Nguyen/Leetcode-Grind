def numberOfSubArrays(nums: list[int], k: int) -> int:
    # Convert array to 1s and 0s, 1 is odd 0 is even

    binaryArr = [] 

    for num in nums:
        if num % 2 == 0:
            binaryArr.append(0)
        else:
            binaryArr.append(1)
    
    # Prefix sum 
    prefixArr = []
    total = 0
    for num in binaryArr:
        total += num
        prefixArr.append(total)
    
    freq = {0: 1}

    # Count
    count = 0 
    for sum in prefixArr:
        if sum - k in freq:
            count += freq[sum - k]
        freq[sum] = 1 + freq.get(sum, 0) 

    return count

print(numberOfSubArrays([2,2,2,1,2,2,1,2,2,2], 2))