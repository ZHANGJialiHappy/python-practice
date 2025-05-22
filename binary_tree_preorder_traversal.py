from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        stack=[]
        head=root
        
        while stack or head:
            if head:
                res.append(head.val)
                stack.append(head.right)
                head=head.left
            else:
                head=stack.pop()
                
        return res
                