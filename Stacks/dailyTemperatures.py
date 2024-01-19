def dailyTemperature(temperatures: list[int]) -> list[int]:
    # Stack will store a list [stackTemp, stackIndex]
    stack = []
    # Array with default value of 0's
    answer = [0] * len(temperatures)

    for currentIndex, currentTemp in enumerate(temperatures):
        while stack and currentTemp > stack[-1][0]:
            stackTemp, stackIndex = stack.pop()
            answer[stackIndex] = currentIndex - stackIndex
        
        stack.append(currentTemp, currentIndex)

    return answer