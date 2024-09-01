"""
226. Invert Binary Tree
Problem Link: https://leetcode.com/problems/invert-binary-tree/description/
"""

from typing import Optional
from src.models.TreeNode import TreeNode

class InvertBinaryTree:
    def invertTree(self, root: Optional[TreeNode]) -> Optional:
        if not root:
           return root

        self.invertTree(root.left)
        self.invertTree(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp

        return root 