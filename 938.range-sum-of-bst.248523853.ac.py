# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
ex1.
         *10
         /  \
       *5    *15
       / \     \
      3   *7    18
      
ex2.
                *10
               /    \
              5      15
             / \     / \
            3   *7  13  18
           /   /
         1    *6
'''
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def dfs(node):
            if node:
                if L<= node.val <= R:
                    self.ans += node.val
                    #print(node.val)
                if node.val>L:
                    dfs(node.left)
                if node.val<R:
                    dfs(node.right)
        self.ans = 0
        dfs(root)
        return self.ans
