# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        #find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == None:
                break
        
        l2 = slow.next
        slow.next = None
        
        #reverse second half
        l1 = head
        cur = l2
        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        #reorder
        
        while l1 and prev:
            next1 = l1.next
            next2 = prev.next
            l1.next = prev
            prev.next = next1
            l1 = next1
            prev = next2

        