# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = deque()
        if not root:
            return None
        stack.append(root)
        
        while stack:
            temp = stack.popleft()
            tempr = temp.right if temp.right else None
            templ = temp.left if temp.left else None
            if templ:
                stack.append(temp.left)
            if tempr:
                stack.append(temp.right)  
            temp.left = tempr 
            temp.right = templ 
        return root




        