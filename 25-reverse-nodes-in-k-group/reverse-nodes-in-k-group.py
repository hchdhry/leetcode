class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
      
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1
        
        if count < k:
            return head
        

        prev = None
        curr = head
        for _ in range(k):
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        head.next = self.reverseKGroup(curr, k)
        
        return prev