class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        
       
        if length == n:
            return head.next
        
     
        target = length - n
        curr = head
        for _ in range(target - 1):
            curr = curr.next
        
     
        curr.next = curr.next.next
        
        return head