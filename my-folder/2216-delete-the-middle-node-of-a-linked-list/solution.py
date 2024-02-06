# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head.next == None or head == None:
            return None
        
        nodes = []

        current = head

        while current:
            nodes.append(current)
            current = current.next

        middle = math.floor(len(nodes) / 2)

        nodes[middle].next = None
        if middle == len(nodes) - 1:
            nodes[middle - 1].next = None
        else:
            nodes[middle - 1].next = nodes[middle + 1]

        return head
