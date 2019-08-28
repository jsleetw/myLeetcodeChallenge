class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """
        use fibonacci
        time O(n)
        space O(2)
        """
        
        a = [0, 1]
        for i in range(n):
            a[0], a[1] = a[1], a[0] + a[1]
        
        return a[1]
