class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        long_str = max(strs)
        short_str = min(strs)

        for k, v in enumerate(short_str):
            if v != long_str[k]:
                return long_str[0:k]

        return short_str
