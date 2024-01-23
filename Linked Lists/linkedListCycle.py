class Node: 
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class Solution:
    def hasCycle(self, head: Node) -> bool:
        fast = head
        slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
        
        return False