# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, root in enumerate(lists):
            heapq.heappush(heap, (root.val, i, root))

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i, root = heapq.heappop(heap)

            curr.next = root
            curr = curr.next

            if root.next:
                root = root.next
                heapq.heappush(heap, (root.val, i, root))

        return dummy.next