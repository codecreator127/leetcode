# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        tail2 = head.next
        num2 = head.next
        num1 = head

        while num2 and num2.next:
            num1.next = num1.next.next
            num2.next = num2.next.next

            if num1.next:
                num1 = num1.next

            if num2.next:
                num2 = num2.next

        num1.next = tail2
        return head
