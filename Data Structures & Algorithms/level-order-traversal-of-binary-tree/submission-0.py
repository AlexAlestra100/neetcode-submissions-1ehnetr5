# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        curr = root

        arr = []

        def dfs(curr, level):
            if not curr:
                return

            if len(arr) < level + 1:
                arr.append([])
            
            arr[level].append(curr.val)

            dfs(curr.left, level + 1)
            dfs(curr.right, level + 1)

            return

        dfs(curr, 0)

        return arr