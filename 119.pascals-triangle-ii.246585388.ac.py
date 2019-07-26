class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex <1:
            return [1]
        
        def helper(prev):
            res = []
            for i in range(len(prev) -1):
                res.append(prev[i]+prev[i+1])
            return [1] + res + [1]

        ans = [[1]]
        for x in range(rowIndex):
            ans.append(helper(ans[-1]))        

        return ans[rowIndex]
