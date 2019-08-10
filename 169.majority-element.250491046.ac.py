class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        nums_set = set(nums)
        for i in nums_set:
            dict[i] = nums.count(i)
        return max(dict, key=dict.get)
