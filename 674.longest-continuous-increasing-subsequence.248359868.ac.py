class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)<1:
            return 0
        
        count = 1
        max_count = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 0:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 1
        
        return max_count
