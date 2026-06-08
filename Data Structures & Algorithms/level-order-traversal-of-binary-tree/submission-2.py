# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelQ = []
        if not root:
            return levelQ

        res = []
        levelQ.append(root)

        while levelQ:
            level = []
            for i in range(len(levelQ)):
                curr = levelQ.pop(0)

                if curr:
                    level.append(curr.val)

                if curr.left:
                    levelQ.append(curr.left)

                if curr.right:
                    levelQ.append(curr.right)

            res.append(level)

        return res