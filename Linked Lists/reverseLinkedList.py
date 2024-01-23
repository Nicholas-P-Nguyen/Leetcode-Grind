class Node: 
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class Solution:
    def reverseList(self, head: Node):
        previousNode = None
        while head:
            temp = head.next
            head.next = previousNode
            previousNode = head
            head = temp
        
        return head