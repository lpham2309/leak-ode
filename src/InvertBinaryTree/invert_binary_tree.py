"""
226. Invert Binary Tree
Problem Link: https://leetcode.com/problems/invert-binary-tree/description/
"""

from typing import Optional
from src.models.TreeNode import TreeNode

class InvertBinaryTree:
    """
    Recursive Solution
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional:
        if not root:
           return root

        self.invertTree(root.left)
        self.invertTree(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp

        return root
    """
    Iterative Solution
    """
    def invertTreeIterative(self, root: Optional[TreeNode]) -> Optional:
        if root:
            queue = [root]

            while queue:
                curr_node = queue.pop(0)
                if curr_node.left:
                    queue.append(curr_node.left)
                elif curr_node.right:
                    queue.append(curr_node.right)
        return root