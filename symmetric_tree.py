# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if not root1 and not root2:
                return True
            elif (not root1 or not root2) or (root1.val!=root2.val):
                return False
            else:
                return dfs(root1.left, root2.right) and dfs (root1.right, root2.left)
            
        if not root:
            return True
        return dfs(root.left, root.right)
    
    # def check(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    #     if root1==None and root2==None:
    #         return True
        
    #     if root1==None or root2==None:
    #         return False
        
    #     if root1.val==root2.val:
    #         return self.check(root1.left, root2.right) and self.check(root1.right, root2.left)