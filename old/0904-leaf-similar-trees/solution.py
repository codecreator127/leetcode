# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, leaves):
        if not root:
            return

        if not root.left and not root.right:
            leaves.append(root.val)
        
        self.dfs(root.left, leaves)
        self.dfs(root.right, leaves)
            
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        lf1 = []
        lf2 = []

        self.dfs(root1, lf1)
        self.dfs(root2, lf2)

        return lf2 == lf1
