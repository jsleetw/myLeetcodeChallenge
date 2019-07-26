# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def swap(head):
            if not head or not head.next:
                return head
            node_next = head.next
            head.next = swap(node_next.next)
            node_next.next = head
            return node_next
        return swap(head)

