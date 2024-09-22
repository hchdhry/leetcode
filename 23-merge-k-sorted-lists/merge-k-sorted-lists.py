import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge case: if the input list is empty
        if not lists:
            return None

        # Initialize the merged list with a dummy head
        mergedlist = ListNode(0)
        curr = mergedlist
        heap = []

      
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))


        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return mergedlist.next