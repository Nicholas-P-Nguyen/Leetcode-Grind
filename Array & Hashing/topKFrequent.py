def topKFrequent(nums: list[int], k: int) -> list[int]:
    hashMap = {}
    frequency = [[] for i in range(len(nums) + 1)]

    # Time complexity O(n) we have to go iterate through the whole nums array 
    # Where n is the size of the nums array 
    for number in nums:
        hashMap[number] = 1 + hashMap.get(number, 0)

    # Time complexity O(n) we have to iterate through the whole hashmap 
    # Where n is the size of the hashmap 
    for number, occurance in hashMap.items():
        # At the index of the # of occurance we append the number 
        frequency[occurance].append(number)

    output = [] 

    # Time complexity O(n) we have to iterate through the frequency array 
    # Where n is the size of the frequency array 
    for i in range(len(frequency) - 1, 0, -1):
        for currentNumber in frequency[i]:
            output.append(currentNumber)
            if len(output) == k:
                return output

print(topKFrequent([1,1,1,2,2,3], 2))

# Time complexity: O(n + n + n) = O(3n) => drop the constant O(n)
# Space complexity: O(n + n + n) = O(3n) => drop the constant O(n) 