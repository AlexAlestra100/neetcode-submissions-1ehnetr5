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
        deepStart = Node(0)
        copy = {None: None}

        start = deepStart
        curr = head
        while curr:
            start.next = Node(curr.val)
            copy[curr] = start.next

            start = start.next
            curr = curr.next

        curr = head
        while curr:
            copy[curr].random = copy[curr.random]
            curr = curr.next

        return deepStart.next