class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        is_neg = False
        
        if(x<0):
            x = abs(x)
            is_neg = True
        
        while x != 0:
            pop = x % 10
            x /= 10
            #print(pop)
            if (rev > 2**31/10) or (rev == 2**31/10 and pop > 7): return 0
            rev = rev * 10 + pop
            
        if is_neg:
            rev = - rev
            
        return rev
