class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <1:
            return []

        def helper(prev):
            res = []
            for i in range(len(prev) -1):
                res.append(prev[i]+prev[i+1])
            return [1] + res + [1]

        ans = [[1]]
        for x in range(numRows-1):
            ans.append( helper( ans[-1] ) )

        return ans

