'''
Given an array of integers a, your task is to calculate the digits that occur the most 
number of times in the array. Return the array of these digits in ascending order.

For a = [25, 2, 3, 57, 38, 41], the output should be solution(a) = [2, 3, 5].
'''
def question_2(a: list[int]):
    toString = ""
    for number in a:
        toString += str(number)
        
    hashMap = {}
    
    for digit in toString:
        hashMap[digit] = 1 + hashMap.get(digit, 0)
    
    print(hashMap)
    
    max_freq = max(hashMap.values())
    
    output = []
    for number, freq in hashMap.items():
        if freq == max_freq:
            output.append(int(number))
    
    output.sort()
    return output