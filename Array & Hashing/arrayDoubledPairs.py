def canReorderDoubled(arr: list[int]) -> bool: 
    hashMap = {}
    for num in arr:
        hashMap[num] = 1 + hashMap.get(num, 0)

    for num in arr:
        if hashMap.get(num, 0) == 0:
            continue

        if num < 0:
            double = num * 2  # Use the absolute value for the double
            if hashMap.get(double, 0) == 0:
                return False
        else:
            double = num // 2  # Use the double for positive numbers
            if hashMap.get(double, 0) == 0:
                return False

        hashMap[num] -= 1
        hashMap[double] -= 1

    return True