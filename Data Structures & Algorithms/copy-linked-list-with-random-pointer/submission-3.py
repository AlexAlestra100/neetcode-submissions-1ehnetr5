"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)

        lList = {None: None}
        start = head
        startB = dummy

        while start:
            startB.next = Node(start.val)
            startB = startB.next

            lList[start] = startB

            start = start.next

        start = head
        startB = dummy.next

        while start:
            startB.random = lList[start.random]

            start = start.next
            startB = startB.next

        return dummy.next
