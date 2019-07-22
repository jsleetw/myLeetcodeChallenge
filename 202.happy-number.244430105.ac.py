class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mem = set()
        
        while n != 1:
            sum = 0
            for i in str(n):
                sum += int(i)*int(i)
            n = sum
            #avoid unstop loop
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True
