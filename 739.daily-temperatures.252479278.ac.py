class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(T)
        stack = []
        for k, v in enumerate(T):
            while stack and T[stack[-1]] < v:
                cur = stack.pop()
                ans[cur] = k - cur
            stack.append(k)
        return ans
