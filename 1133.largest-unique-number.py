#https://leetcode.com/problems/largest-unique-number/
class Solution(object):
    def largestUniqueNumber(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A = sorted(A)
        A = A[::-1]
        index = set(A)
        ans = []
        for i in index:
            Atmp = A
            Atmp.remove(i)
            if i not in Atmp:
               ans.append(i)
        if ans:
            return max(ans)
        else:
            return -1
