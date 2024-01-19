class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # Checking it's there are values in the stack 
        if self.minStack:
            # Updating val to be the min value at the current point in the stack 
            val = min(val, self.minStack[-1])
        # If min value found append to minStack otherwise if the stack was empty append to the minStack
        self.minStack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

    