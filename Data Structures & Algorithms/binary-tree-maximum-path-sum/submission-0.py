# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximum = float("-inf")


        def dfs(node):
            if node is None:
                return 0

            left_path = max(0, dfs(node.left))
            right_path = max(0, dfs(node.right))

            self.maximum = max(
            self.maximum,
            node.val + left_path + right_path
            )
            return node.val + max(left_path, right_path)

        dfs(root)
        return self.maximum