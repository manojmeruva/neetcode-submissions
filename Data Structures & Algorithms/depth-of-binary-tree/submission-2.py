# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        if not root:
            return 0
        queue.append(root)
        answer = 0
        prevLen = 0
        popcount = 0
        while queue:
            if popcount == prevLen:
                answer+=1
                prevLen = len(queue)
                popcount = 0
            temp = queue.popleft()
            popcount +=1
        
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            
        return answer

        