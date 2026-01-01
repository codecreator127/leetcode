# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node: TreeNode, maximum):
        if not node:
            return 0

        if node.val < maximum:
            return self.dfs(node.left, maximum) + self.dfs(node.right, maximum)
        else:
            return 1 + self.dfs(node.left, node.val) + self.dfs(node.right, node.val)


    def goodNodes(self, root: TreeNode) -> int:
        
        return 1 + self.dfs(root.left, root.val) + self.dfs(root.right, root.val)
