# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
        
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def bfs(start: int, end:int) -> TreeNode:
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = bfs(start, mid-1)
            root.right = bfs(mid+1, end)
            return root
        return bfs(0, len(nums)-1)
                
     
    
