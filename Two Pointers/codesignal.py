def solution(a, k):
    def count_ribbons(length):
        count = 0
        for ribbon in a:
            count += ribbon // length
        return count
    
    left, right = 1, max(a)
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if count_ribbons(mid) >= k:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result


solution([5,2,7,4,9], 5)