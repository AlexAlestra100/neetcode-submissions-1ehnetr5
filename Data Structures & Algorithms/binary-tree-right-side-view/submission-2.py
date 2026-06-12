# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(curr, i):
            if not curr:
                return
            
            print(curr.val, i)

            if i == len(res):
                res.append(curr.val)
            dfs(curr.right, i + 1)
            dfs(curr.left, i + 1)

            return

        dfs(root, 0)

        return res