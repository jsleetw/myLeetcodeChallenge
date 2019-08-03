# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def get_all_node(node_child, ret_arr, curr_sum):
            if node_child:
                if not node_child.left and not node_child.right:
                    curr_sum += node_child.val
                    if curr_sum == sum:
                        rets.append(ret_arr)
                ret_arr.append(node_child.val)
                curr_sum += node_child.val
                get_all_node(node_child.left, ret_arr[:], curr_sum)
                get_all_node(node_child.right, ret_arr[:], curr_sum)
    
        rets = []
        get_all_node(root, [], 0)
        return rets
