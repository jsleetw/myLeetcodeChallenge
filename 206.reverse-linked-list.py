# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# T: O(n)
# S: O(1)
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev_list = None
        current_list = head

        while current_list is not None:
            next_point = current_list.next
            current_list.next = prev_list
            prev_list = current_list
            current_list = next_point

        return prev_list
