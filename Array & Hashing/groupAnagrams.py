
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    output = {}

    for word in strs: 
        charCount = [0] * 26

        for char in word:
            charCount[ord(char) - ord("a")] += 1

        tupleCharCount = tuple(charCount)

        if tupleCharCount in output:
            output[tupleCharCount].append(word)
        else:
            output[tupleCharCount] = [word]

    return list(output.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# Time complexity O(m * n) where m is the size of the array and n is the size of each word
# Space O(n) where n is each word being placed into the hashmap 
