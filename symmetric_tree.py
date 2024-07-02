# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.check(root.left, root.right)
    
    def check(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1==None and root2==None:
            return True
        
        if root1==None or root2==None:
            return False
        
        if root1.val==root2.val:
            return self.check(root1.left, root2.right) and self.check(root1.right, root2.left)