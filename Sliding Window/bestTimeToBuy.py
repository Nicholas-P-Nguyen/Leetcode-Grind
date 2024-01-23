def maxProfit(prices: list[int]) -> int:
    left = 0
    output = 0

    for right in range(1, len(prices)):
        if prices[left] > prices[right]:
            
            left = right
        
        output = max(prices[right] - prices[left], output)
    
    return output

print(maxProfit([7,1,5,3,6,4]))
        