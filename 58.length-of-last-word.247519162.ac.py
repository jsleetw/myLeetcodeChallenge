class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = s.split(" ")
        
        for i in arr[::-1]:
            if i:
                return len(i)
        return 0
