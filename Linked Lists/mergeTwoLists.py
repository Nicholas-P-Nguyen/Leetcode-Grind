class Node: 
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class Solution:
    def mergeTwoLists(self, list1: Node, list2: Node):
        '''
        Create a dummy node to avoid edge cases and streamline the merging process. 
        tail is initialized to dummy and keeps track of the last node 
        '''
        dummy = Node()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                # Increment list1
                list1 = list1.next
            else:
                tail.next = list2
                # Increment list2
                list2 = list2.next
            # Increment tail after checking which value is smaller
            tail = tail.next
        # If there are still values in list1 or list2 
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        # dummy is the place holder node. The head of the merge list starts after the dummy node
        return dummy.next
            

            