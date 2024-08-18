# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
   
        
        while curr:
            curr = curr.next
            length +=1
        

        if length == n:
            return head.next
        
        length = length-n
        curr = head

        for _ in range(length-1):
            curr = curr.next
           
        curr.next = curr.next.next
        
        return head





