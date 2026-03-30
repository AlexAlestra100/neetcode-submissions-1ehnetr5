# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tup = [None, 0, k - 1]

        def dfs(curr):
            nonlocal tup
            if not curr:
                return

            dfs(curr.left)
            if tup[1] == tup[2]:
                tup[0] = curr.val
                tup[1] += 1
                return
            tup[1] += 1
            dfs(curr.right)

            return
            
        dfs(root)

        return tup[0]