def isPalindrome(s: str) -> bool:
    alphanumericString = ""

    for char in s:
        if char.isalpha() or char.isnumeric():
            alphanumericString += char.lower()

    left = 0
    right = len(alphanumericString) - 1

    while left < right:
        if alphanumericString[left] == alphanumericString[right]:
            left += 1
            right -= 1
        else:
            return False
    
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))

# Time complexity O(n) where n is the size of the input string.
# Space complexity O(1) because we just create memory for the pointers. 
# Lesson: Read the problem THOROUGHLY! It says to convert the string. I didn't do that initially. 