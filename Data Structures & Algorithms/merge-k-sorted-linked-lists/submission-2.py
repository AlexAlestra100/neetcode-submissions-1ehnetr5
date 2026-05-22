# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, root in enumerate(lists):
            heapq.heappush(heap, (root.val, i))

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i = heapq.heappop(heap)

            curr.next = lists[i]
            curr = curr.next

            if lists[i].next:
                lists[i] = lists[i].next
                
                heapq.heappush(heap, (lists[i].val, i))

        return dummy.next