# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = True
        def dfs(root,subRoot):
            nonlocal res
            if not root:
                return False
            if root.val == subRoot.val:
                res = self.isSameTree(root,subRoot)
                if res:
                    return res
            left = self.isSubtree(root.left,subRoot) 
            right = self.isSubtree(root.right,subRoot)
            return left or right
        return dfs(root,subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        res = True

        def dfs(p,q):
            nonlocal res
            if not p and not q:
                return
            if (not p and q) or (not q and p):
                res = False
                return
                
            if p.val != q.val:
                res = False
                return

            dfs(p.left,q.left)
            dfs(p.right,q.right)

            return
        dfs(p,q)
        return res
        