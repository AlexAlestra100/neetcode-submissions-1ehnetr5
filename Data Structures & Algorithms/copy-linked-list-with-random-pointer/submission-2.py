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
        hMap = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            hMap[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = hMap[curr]
            copy.next = hMap[curr.next]
            copy.random = hMap[curr.random]
            curr = curr.next

        return hMap[head]