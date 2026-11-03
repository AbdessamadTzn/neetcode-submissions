# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy =  ListNode(0, head)
        groupPrev = dummy

        while True:

            kth = groupPrev
            for i in range(k):
                if not kth:
                    break
                kth = kth.next
            
            if not kth:
                break
            #node just after group
            groupNext = kth.next
            #prepare reverse

            prev = groupNext
            curr = groupPrev.next

            while curr is not groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            
            oldStart = groupPrev.next
            groupPrev.next = kth
            groupPrev = oldStart
        
        return dummy.next


        

