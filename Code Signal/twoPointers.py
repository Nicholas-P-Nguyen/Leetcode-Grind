def solution(a: list[int]):
    left = 0 
    right = len(a) - 1
    
    b = []
    
    while left < right:
        b.append(a[left])
        b.append(a[right])
        left += 1
        right -= 1
      
    if len(a) % 2 != 0:
        b.append(a[len(a) // 2])
        
    for i in range(len(b) - 1):
        if b[i] >= b[i + 1]:
            return False
    
    return True