def numPairsDivisibleBy60(time: list[int]) -> int:
    counter = 0
    # Creating a bucket count index is the number needed for get a number divisible by 60
    count  = [0] * 60
    for one in range(len(time)):
        index = time[one] % 60
        # If pair is found increment by the value at that index
        counter += count[(60 - index)%60] 
        # Increment the value by 1 in case pair is found 
        count[index] += 1
    return counter

numPairsDivisibleBy60([30, 20, 150, 100, 40])