#https://leetcode.com/problems/armstrong-number/
class Solution(object):
    def isArmstrong(self, N):
        """
        :type N: int
        :rtype: bool
        """
        str_N = str(N)
        num = 0
        for i in str_N:
            num += pow(int(i), len(str_N))
        return num == N
