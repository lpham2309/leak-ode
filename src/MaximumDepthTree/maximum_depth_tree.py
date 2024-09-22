"""
104. Maximum Depth of Binary Tree
Problem Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
"""
from src.models.TreeNode import TreeNode

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = 0
        self.bfs(root, max_depth, 0, 0)

    def bfs(self, root, max_depth, max_left, max_right):
        if not root:
            return 0
        if root.left:
            max_left = self.bfs(root, max_depth, max_left, 0)
        if root.right:
            max_right = self.bfs(root, max_depth, 0, max_right)

        return 1 + max(max_left, max_right)