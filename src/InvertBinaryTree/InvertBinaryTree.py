from typing import Optional
from models.TreeNode import TreeNode 

class InvertBinaryTree():
    def invertTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
           return root

        self.invertTree(root.left)
        self.invertTree(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp

        return root 