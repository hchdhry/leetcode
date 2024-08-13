class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Find the middle of the list
        middle = self.findMiddle(head)
        
        # Split the list
        second_half = middle.next
        middle.next = None
        
        # Reverse the second half
        second_half = self.reverseList(second_half)
        
        # Merge the two halves
        self.mergeLists(head, second_half)

    def findMiddle(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        return prev

    def mergeLists(self, l1, l2):
        while l2:
            next_l1 = l1.next
            next_l2 = l2.next

            l1.next = l2
            l2.next = next_l1

            l1 = next_l1
            l2 = next_l2