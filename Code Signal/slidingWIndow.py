def solution(a: list[int], m, k):
    count = 0
    print(len(a))
    for i in range(len(a) - m + 1):
        subarray = a[i:i+m]
        for j in range(len(subarray)):
            for l in range(j+1,len(subarray)):
                if subarray[j] + subarray[l] == k:
                    count += 1
                    break
            else:
                continue
            break
    return count
        
solution([2, 4, 7, 5, 3, 5, 8, 5, 1, 7], 4, 10)