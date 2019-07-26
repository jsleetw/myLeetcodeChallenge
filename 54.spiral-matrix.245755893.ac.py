class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        s = []
        while matrix:
            s += matrix.pop(0)
            matrix = zip(*matrix)
            matrix.reverse()
        
        return s
