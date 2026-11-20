# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        before = dummy

        for i in range(left -1):
            before = before.next

        
        start = before.next

        curr = start
        prev = None



        for i in range(right - left + 1): 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        before.next = prev
        start.next = curr
    
        return dummy.next


        