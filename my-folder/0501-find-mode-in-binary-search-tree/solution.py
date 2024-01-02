# Definition for a binary tree root.
# class Treeroot:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def inorder_traversal(root, max_freq, current_freq, prev_value, modes):
            if root is None:
                return max_freq, current_freq, prev_value, modes

            # Traverse left subtree
            max_freq, current_freq, prev_value, modes = inorder_traversal(
                root.left, max_freq, current_freq, prev_value, modes)

            # Process current root
            if root.val == prev_value:
                current_freq += 1
            else:
                current_freq = 1

            if current_freq > max_freq:
                max_freq = current_freq
                modes = [root.val]
            elif current_freq == max_freq:
                modes.append(root.val)

            prev_value = root.val

            # Traverse right subtree
            return inorder_traversal(
                root.right, max_freq, current_freq, prev_value, modes)

        if root is None:
            return []

        max_freq, current_freq, prev_value, modes = inorder_traversal(
            root, 0, 0, None, [])

        return modes
