'''
Given an array of integers a, your task is to count the number of pairs i and j 
(where 0 ≤ i < j < a.length), such that a[i] and a[j] are digit anagrams.

Two integers are considered to be digit anagrams if they contain the same digits. 
In other words, one can be obtained from the other by rearranging the digits (or trivially, 
if the numbers are equal). For example, 54275 and 45572 are digit anagrams, but 321 and 782 
are not (since they don't contain the same digits). 220 and 22 are also not considered as digit 
anagrams, since they don't even have the same number of digits.

'''

def question_1(a: list[int]):
    hashMap = {}
    counter = 0
    numToString = []
    for num in a:
        numToString.append(str(num))
    
    for number in numToString:
        # Using the bucket sort method index is the digit/value is # of pairs
        intCount = [0] * 10      
        for digit in number:
            intCount[int(digit)] += 1
        
        tupleIntCount = tuple(intCount)
        
    
        if tupleIntCount not in hashMap:
            hashMap[tupleIntCount] = 1
        else:
            # Pair is found so increment count by the count in map
            counter += hashMap[tupleIntCount]
            # Increment value in map in case pair is found again. 
            hashMap[tupleIntCount] += 1
            
    return counter