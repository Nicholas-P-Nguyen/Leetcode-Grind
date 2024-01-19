class Stack:

    def __init__(self):
        self.stack = []
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0
        
    def push(self, item):
        self.stack.append(item)
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from an empty list")
        else:
            output = self.stack[-1]
            del self.stack[-1]
            self.size -= 1
            return output

    def peek(self):
        if self.isEmpty():
            raise IndexError("peeking from an empty list")
        return self.stack[-1]
    
    def size(self) -> int:
        return self.size()
    

        
        
