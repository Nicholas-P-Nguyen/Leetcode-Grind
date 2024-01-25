def solution(a: list[int], k):
    count = 0 
    hashMap = {}
    
    for num in a:
        remainder = num % k
        complement = (k - remainder) % k
        
        if complement in hashMap:
            count += hashMap[complement]
            
        hashMap[remainder] = 1 + hashMap.get(remainder, 0) 
        
    return count