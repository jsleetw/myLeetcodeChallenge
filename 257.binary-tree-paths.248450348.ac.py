# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def node_to_str(node_child, ret_str):
            if node_child:
                ret_str += str(node_child.val)
                if not node_child.left and not node_child.right:
                    rets.append(ret_str)
                else:
                    ret_str += "->"
                    node_to_str(node_child.left, ret_str)
                    node_to_str(node_child.right, ret_str)
        
        rets = []
        node_to_str(root,'')
        return rets
