# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        
        if guess(n) == 0:
            return n
        
        while left < right:
            mid = (right + left) / 2
            res = guess(mid)
            print(mid,res)
            if res == -1:
                right = mid
            elif res == 1:
                left = mid + 1
            elif res == 0:
                return mid
        return left
            
