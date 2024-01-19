def isValid(s: str) -> bool:
    validParenthesis = {')' : '(',
                        ']' : '[',
                        '}' : '{'}
    
    stack = []

    for currentParenthesis in s:
        if currentParenthesis not in validParenthesis:
            stack.append(currentParenthesis)
        else:
            # Have to check if the stack is not empty AND the last item (open parenthesis) in the stack is equal current parenthesis value in the hashmap
            if stack and stack[-1] == validParenthesis[currentParenthesis]:
                stack.pop()
            else: 
                return False
    
    if not stack:
        return True
    else:
        return False

print(isValid("()"))

# Time complexity: O(n) where n is the size of the input string 
# Space complexity: O(n) where n is the size of the hashmap 