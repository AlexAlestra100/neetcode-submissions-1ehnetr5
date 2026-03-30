# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 0

        def dfs(curr, prevVal):
            nonlocal goodNodes

            pV = prevVal

            if curr.val >= prevVal:
                goodNodes += 1
                pV = curr.val

            if curr.left:
                dfs(curr.left, pV)

            if curr.right:
                dfs(curr.right, pV)

            return
            
        dfs(root, root.val)

        return goodNodes