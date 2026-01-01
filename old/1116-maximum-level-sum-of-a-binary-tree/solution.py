# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = {}
        level = 1

        def BFS(root, level):
            if not root:
                return []
            if level not in ans:
                ans[level] = root.val
            else:
                ans[level] += root.val

            BFS(root.left, level + 1)
            BFS(root.right, level + 1)

        BFS(root, level)
        print(ans)

        largest = float("-inf")
        for key in ans.keys():
            if ans[key] > largest:
                largest = ans[key]
                output = key

        return output

