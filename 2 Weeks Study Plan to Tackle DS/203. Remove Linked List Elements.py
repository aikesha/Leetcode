"""
Given the head of a linked list and an integer val, remove all the nodes of 
the linked list that has Node.val == val, and return the new head.

Example 2:

Input: head = [], val = 1
Output: [] 

Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return 
            
        dummyNode = ListNode(next = head)
        tail = dummyNode
        
        while tail.next:
            if tail.next.val == val:
                tail.next = tail.next.next
            else:
                tail = tail.next
    
        return dummyNode.next


