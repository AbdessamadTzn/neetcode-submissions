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
        
            if fast == slow:
                break
        
        #split
        l2 = slow.next
        slow.next = None
        
        #reverse second half
        current = l2
        prev = None

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        #reorder (no sorting)
        l1 = head

        while l1 and prev:   
        #l2 it's prev here after reversing, prev point to head of l2 reversed

            nxt1 = l1.next
            nxt2 = prev.next
            l1.next = prev
            prev.next = nxt1
            prev = nxt2
            l1 = nxt1



        
       

        