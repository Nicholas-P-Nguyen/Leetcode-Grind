def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    sHash = {}
    tHash = {}

    for char in s:
        if char not in sHash:
            sHash[char] = 1
        else:
            sHash[char] += 1
    
    for char in t:
        if char not in tHash:
            tHash[char] = 1
        else:
            tHash[char] += 1
    
    if sHash == tHash:
        return True
    
    return False

# Time complexity O(n + n) because we iterate through each string and put it into the hashmap
# Space: O(n + n) because we create new hashmaps and input them into the hashmaps 

print(isAnagram("rat", "tar"))