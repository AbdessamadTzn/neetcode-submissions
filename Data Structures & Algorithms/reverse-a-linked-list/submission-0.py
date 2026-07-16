# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous_node = None
        while current:
            nxt = current.next
            current.next = previous_node
            previous_node = current
            current = nxt

        return previous_node
