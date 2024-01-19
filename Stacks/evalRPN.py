def evalRPN(tokens: list[str]) -> int:
    stack = [] 
    validOperators = ["+", "-", "/", "*"]

    for token in tokens:
        if token not in validOperators:
            stack.append(int(token))
        else:
            numOne = stack.pop()
            numTwo = stack.pop()
            result = evaluate(numOne, numTwo, token)
            stack.append(int(result))
    
    return stack[0]
        

def evaluate(numOne, numTwo, operator) -> int:
    if operator == "+":
        return numTwo + numOne
    elif operator == "-":
        return numTwo - numOne
    elif operator == "/":
        # Have to cast an int to ensure the result rounds down 
        return int(numTwo / numOne)
    else:
        return numTwo * numOne
    

print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

# Time complexity: O(n) where n is the size of the tokens array. The time complexity is longer because we're branching to another function 
# Space complexity: O(n + 4) where n is the size of the stack + the size of the validOperators array 

# Neetcode's solution 

def neetEvalRPN(tokens: list[str]) -> int:
    stack = []
    for token in tokens:
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "-":
            numOne = stack.pop()
            numTwo = stack.pop()
            stack.append(numTwo - numOne)
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        elif token == "/":
            numOne = stack.pop()
            numTwo = stack.pop()
            stack.append(int(numTwo / numOne))
        else:
            stack.append(int(token))
    
    return stack[0]