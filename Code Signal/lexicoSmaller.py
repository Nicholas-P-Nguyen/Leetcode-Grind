def solution(s: str, t: str):
    count = 0
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']    
    
    
    for index, char in enumerate(s):
        temp = ""
        if char in digits:
            temp = s[:index] + s[index + 1:]
            
            if temp < t:
                count += 1
                continue
    
    for index, char in enumerate(t):
        temp = ""
        if char in digits:
            temp = t[:index] + t[index + 1:]
            
            if temp > s: 
                count += 1
                continue
    
    return count