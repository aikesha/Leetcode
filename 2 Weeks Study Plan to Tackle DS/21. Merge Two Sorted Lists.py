"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by 
splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 2:

Input: list1 = [], list2 = []
Output: []
"""

# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def __init__(self):
        self.head = None
    
    def addToList(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode
        
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = Node(0)
        tail = dummyNode
        while True:
            if list1 is None:
                tail.next = list2
                break
            
            if list2 is None:
                tail.next = list1
                break
                
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
        
        return dummyNode.next

